from uuid import UUID, uuid4
from pydantic import BaseModel, Field
from typing import Optional, List


class Route(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    city_a: str
    city_b: str
    length: int
    color: Optional[str] = None
    locomotive: int
    tunnel: bool = False
    claimed_by: Optional[UUID] = None
    stations: List[str] = Field(default_factory=list)

    def is_claimed(self) -> bool:
        return self.claimed_by is not None
