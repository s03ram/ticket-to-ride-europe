from uuid import uuid4, UUID
from pydantic import BaseModel
from typing import Optional

class Route(BaseModel):
    id: int
    city1: str
    city2: str
    length: int
    color: Optional[str] = None
    locomotive: int
    tunnel: bool = False
    claimed_by: Optional[UUID] = None
    stations: list[str] = []

    def is_claimed(self) -> bool:
        return self.is_claimed is not None
