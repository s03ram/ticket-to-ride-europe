from typing import Optional
from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from src.models.city import City


class Route(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    city_a: City
    city_b: City
    length: int
    color: Optional[str] = None
    locomotive: int
    tunnel: bool = False
    claimed_by: Optional[UUID] = None

    def is_claimed(self) -> bool:
        return self.claimed_by is not None
