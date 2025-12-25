from typing import List, Optional
from uuid import UUID

from src.game_state import GameState
from src.models.colors import TrainColor
from src.models.game import GamePhase
from src.models.result_models import (
    ClaimRouteResult,
    DrawCardResult,
    DrawDestinationResult,
)
from src.models.route import Route


class ActionHandler:
    """Handles all player actions and game logic"""

    def __init__(self, game_state: GameState):
        self.state = game_state

    # -------- VALIDATION HELPERS --------

    def validate_player_turn(self, player_id: UUID) -> Optional[str]:
        """Check if it's this player's turn"""
        current_player = self.state.get_current_player()
        if current_player.id != player_id:
            return f"Not your turn. Current player: {current_player.name}"
        return None

    def validate_game_phase(self) -> Optional[str]:
        """Check if game is in playing phase"""
        if self.state.phase not in [GamePhase.PLAYING, GamePhase.FINAL_ROUND]:
            return f"Game is not in play. Current phase: {self.state.phase.value}"
        return None

    # -------- DRAW TRAIN CARDS --------

    def draw_train_cards(
        self, player_id: UUID, face_up_index: Optional[int] = None
    ) -> DrawCardResult:
        """
        Draw train cards. Player can either:
        - Draw from deck (face_up_index=None)
        - Draw a face-up card (face_up_index=0-4)

        Rules:
        - Can draw 2 cards per turn
        - Drawing a face-up locomotive counts as both draws
        - If 3+ locomotives are face-up after drawing, refresh all face-up cards
        """
        # Validation
        if error := self.validate_player_turn(player_id):
            return DrawCardResult(success=False, cards_drawn=[], message=error)

        if error := self.validate_game_phase():
            return DrawCardResult(success=False, cards_drawn=[], message=error)

        if self.state.actions_taken_this_turn >= 1:
            return DrawCardResult(
                success=False,
                cards_drawn=[],
                message="Already took an action this turn",
            )

        player = self.state.get_player(player_id)
        cards_drawn = []

        # First card draw
        if face_up_index is not None:
            # Drawing from face-up cards
            if not (0 <= face_up_index < len(self.state.train_deck.face_up_cards)):
                return DrawCardResult(
                    success=False, cards_drawn=[], message="Invalid face-up card index"
                )

            card = self.state.train_deck.face_up_cards[face_up_index]

            # Check if it's a locomotive
            if card.color == TrainColor.LOCOMOTIVE:
                if self.state.drew_locomotive_this_turn:
                    return DrawCardResult(
                        success=False,
                        cards_drawn=[],
                        message="Cannot draw two locomotives in one turn",
                    )

                # Drawing a face-up locomotive ends your turn
                player.train_cards.append(card)
                self.state.train_deck.replace_face_up_card(face_up_index)
                cards_drawn.append(card)
                self.state.drew_locomotive_this_turn = True
                self.state.actions_taken_this_turn = 2  # Counts as both draws

                # Check for too many locomotives
                if self.state.train_deck.check_too_many_locomotives():
                    self.state.train_deck.refresh_face_up_cards()

                self.state.next_turn()
                return DrawCardResult(
                    success=True,
                    cards_drawn=cards_drawn,
                    message="Drew locomotive (turn ended)",
                )
            else:
                # Regular face-up card
                player.train_cards.append(card)
                self.state.train_deck.replace_face_up_card(face_up_index)
                cards_drawn.append(card)
                self.state.actions_taken_this_turn += 1
        else:
            # Drawing from deck
            card = self.state.train_deck.draw_card()
            if not card:
                return DrawCardResult(
                    success=False, cards_drawn=[], message="No cards left in deck"
                )

            player.train_cards.append(card)
            cards_drawn.append(card)
            self.state.actions_taken_this_turn += 1

        # Check if we need a second draw
        if self.state.actions_taken_this_turn < 2:
            return DrawCardResult(
                success=True,
                cards_drawn=cards_drawn,
                message="Drew 1 card, can draw 1 more",
            )
        else:
            # Turn complete
            self.state.next_turn()
            return DrawCardResult(
                success=True,
                cards_drawn=cards_drawn,
                message=f"Drew {len(cards_drawn)} card(s), turn complete",
            )

    # -------- CLAIM ROUTE --------

    def claim_route(
        self,
        player_id: UUID,
        route_id: str,
        cards_to_use: List[UUID],  # IDs of cards player wants to spend
    ) -> ClaimRouteResult:
        """
        Claim a route on the board

        Rules:
        - Must have enough trains
        - Must have correct cards
        - Route must not be claimed
        - This ends the player's turn
        """
        # Validation
        if error := self.validate_player_turn(player_id):
            return ClaimRouteResult(success=False, message=error)

        if error := self.validate_game_phase():
            return ClaimRouteResult(success=False, message=error)

        if self.state.actions_taken_this_turn >= 1:
            return ClaimRouteResult(
                success=False, message="Already took an action this turn"
            )

        player = self.state.get_player(player_id)
        route = self.state.board.get_route(route_id)

        if not route:
            return ClaimRouteResult(success=False, message="Route not found")

        if route.is_claimed():
            return ClaimRouteResult(success=False, message="Route already claimed")

        # Check trains remaining
        if player.trains_remaining < route.length:
            return ClaimRouteResult(
                success=False,
                message=f"Not enough trains. Need {route.length}, have {player.trains_remaining}",
            )

        # Validate cards
        if len(cards_to_use) != route.length:
            return ClaimRouteResult(
                success=False, message=f"Must use exactly {route.length} cards"
            )

        # Get the actual card objects
        player_card_map = {card.id: card for card in player.train_cards}
        cards = []
        for card_id in cards_to_use:
            if card_id not in player_card_map:
                return ClaimRouteResult(
                    success=False, message="Invalid card ID or card not in hand"
                )
            cards.append(player_card_map[card_id])

        # Validate card colors
        if route.color is not None:
            # Colored route: need matching color + locomotives
            valid_cards = [
                c
                for c in cards
                if c.color == route.color or c.color == TrainColor.LOCOMOTIVE
            ]
            if len(valid_cards) != route.length:
                return ClaimRouteResult(
                    success=False,
                    message=f"Cards must match route color ({route.color.value}) or be locomotives",
                )
        else:
            # Gray route: all cards must be same color (or locomotives)
            non_locomotive_colors = [
                c.color for c in cards if c.color != TrainColor.LOCOMOTIVE
            ]
            if non_locomotive_colors:
                first_color = non_locomotive_colors[0]
                if not all(c == first_color for c in non_locomotive_colors):
                    return ClaimRouteResult(
                        success=False,
                        message="For gray routes, all non-locomotive cards must be the same color",
                    )

        # All validations passed - claim the route!
        self.state.board.claim_route(route_id, player_id)

        # Remove cards from player's hand
        for card in cards:
            player.train_cards.remove(card)

        # Discard the cards
        self.state.train_deck.discard_pile.extend(cards)

        # Deduct trains
        player.trains_remaining -= route.length

        # Award points based on route length
        points_table = {1: 1, 2: 2, 3: 4, 4: 7, 5: 10, 6: 15}
        points = points_table.get(route.length, route.length * 3)
        player.score += points

        # Check if this triggers the final round
        if player.trains_remaining <= 2 and not self.state.final_turn_triggered:
            self.state.final_turn_triggered = True
            self.state.phase = GamePhase.FINAL_ROUND

        # End turn
        self.state.actions_taken_this_turn = 2
        self.state.next_turn()

        return ClaimRouteResult(
            success=True,
            route_id=route_id,
            points_earned=points,
            cards_spent=cards,
            message=f"Claimed route {route.city1}-{route.city2} for {points} points",
        )

    # -------- DRAW DESTINATION TICKETS --------

    def draw_destination_tickets(
        self, player_id: UUID, tickets_to_keep: Optional[List[UUID]] = None
    ) -> DrawDestinationResult:
        """
        Draw destination tickets

        Rules:
        - Draw 3 tickets
        - Must keep at least 1
        - Can keep all 3
        - This ends the player's turn
        """
        # Validation
        if error := self.validate_player_turn(player_id):
            return DrawDestinationResult(success=False, tickets_drawn=[], message=error)

        if error := self.validate_game_phase():
            return DrawDestinationResult(success=False, tickets_drawn=[], message=error)

        if self.state.actions_taken_this_turn >= 1:
            return DrawDestinationResult(
                success=False,
                tickets_drawn=[],
                message="Already took an action this turn",
            )

        player = self.state.get_player(player_id)
        player

        # If no tickets_to_keep provided, we're in the draw phase
        if tickets_to_keep is None:
            tickets = self.state.destination_deck.draw_tickets(3)
            if not tickets:
                return DrawDestinationResult(
                    success=False,
                    tickets_drawn=[],
                    message="No destination tickets available",
                )

            return DrawDestinationResult(
                success=True,
                tickets_drawn=tickets,
                message="Drew tickets, must choose which to keep (at least 1)",
            )

        # Player is choosing which tickets to keep
        if len(tickets_to_keep) < 1:
            return DrawDestinationResult(
                success=False, tickets_drawn=[], message="Must keep at least 1 ticket"
            )

        # Add kept tickets to player's hand
        # (In a real implementation, you'd validate these IDs against recently drawn tickets)
        # For now, we'll trust the tickets_to_keep list

        self.state.actions_taken_this_turn = 2
        self.state.next_turn()

        return DrawDestinationResult(
            success=True,
            tickets_drawn=[],
            message=f"Kept {len(tickets_to_keep)} destination ticket(s)",
        )

    # -------- QUERY METHODS --------

    def get_available_actions(self, player_id: UUID) -> List[str]:
        """Get list of actions the player can currently take"""
        if self.validate_player_turn(player_id) or self.validate_game_phase():
            return []

        if self.state.actions_taken_this_turn >= 2:
            return []

        actions = []

        if self.state.actions_taken_this_turn == 0:
            actions.extend(
                ["draw_train_cards", "claim_route", "draw_destination_tickets"]
            )
        elif (
            self.state.actions_taken_this_turn == 1
            and not self.state.drew_locomotive_this_turn
        ):
            actions.append("draw_train_cards")  # Can draw second card

        return actions

    def get_claimable_routes(self, player_id: UUID) -> List[Route]:
        """Get all routes the player can currently claim"""
        player = self.state.get_player(player_id)
        if not player:
            return []

        return [
            route
            for route in self.state.board.get_available_routes()
            if player.can_claim_route(route)
        ]
