from pydantic import BaseModel
from typing import Optional
from data.models.city import City
from uuid import UUID


class Route(BaseModel):
    city_a: City
    city_b: City
    length: int
    color: Optional[str] = None
    locomotive: Optional[bool] = False
    tunnel: Optional[bool] = False
    claimed_by: Optional[UUID] = None

    def is_claimed(self) -> bool:
        return self.claimed_by is not None
