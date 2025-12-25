from typing import Dict, List, Optional

from pydantic import BaseModel

from src.models.cards import DestinationTicket, TrainCard


class ActionResult(BaseModel):
    """Result of an action attempt"""

    success: bool
    message: str
    data: Optional[Dict] = None


class DrawCardResult(BaseModel):
    """Result of drawing train cards"""

    success: bool
    cards_drawn: List[TrainCard]
    message: str


class ClaimRouteResult(BaseModel):
    """Result of claiming a route"""

    success: bool
    route_id: Optional[str] = None
    points_earned: int = 0
    cards_spent: List[TrainCard] = []
    message: str


class ClaimStationResult(BaseModel):
    """Result of claiming a station"""

    success: bool
    city_id: Optional[str] = None
    station_spent: int
    message: str


class DrawDestinationResult(BaseModel):
    """Result of drawing destination tickets"""

    success: bool
    tickets_drawn: List[DestinationTicket]
    message: str
