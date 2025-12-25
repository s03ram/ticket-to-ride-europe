from enum import Enum
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class CityName(str, Enum):
    """Represents a city in the game"""

    AMSTERDAM = "Amsterdam"
    ANGORA = "Angora"
    ATHINA = "Athina"
    BARCELONA = "Barcelona"
    BERLIN = "Berlin"
    BREST = "Brest"
    BRINDISI = "Brindisi"
    BRUXELLES = "Bruxelles"
    BUCURESTI = "Bucuresti"
    BUDAPEST = "Budapest"
    CADIZ = "Cadiz"
    CONSTANTINOPLE = "Constantinople"
    DANZIG = "Danzig"
    DIEPPE = "Dieppe"
    EDINBURGH = "Edinburgh"
    ERZURUM = "Erzurum"
    ESSEN = "Essen"
    FRANKFURT = "Frankfurt"
    KHARKOV = "Kharkov"
    KOBENHAVN = "Kobenhavn"
    KYIV = "Kyiv"
    LISBOA = "Lisboa"
    LONDON = "London"
    MADRID = "Madrid"
    MARSEILLE = "Marseille"
    MOSKVA = "Moskva"
    MUNCHEN = "Munchen"
    PALERMO = "Palermo"
    PAMPLONA = "Pamplona"
    PARIS = "Paris"
    PETROGRAD = "Petrograd"
    RIGA = "Riga"
    ROMA = "Roma"
    ROSTOV = "Rostov"
    SARAJEVO = "Sarajevo"
    SEVASTOPOL = "Sevastopol"
    SMOLENSK = "Smolensk"
    SMYRNA = "Smyrna"
    SOCHI = "Sochi"
    SOFIA = "Sofia"
    STOCKHOLM = "Stockholm"
    VENEZIA = "Venezia"
    WARSZAWA = "Warszawa"
    WIEN = "Wien"
    WILNO = "Wilno"
    ZAGRAB = "Zagrab"
    ZURICH = "Zurich"


class City(BaseModel):
    """Represents a city in the game"""

    id: UUID = Field(default_factory=uuid4)
    name: CityName
    station_claimed_by: Optional[UUID] = Field(
        None, description="Player ID who claimed the station, if any"
    )
