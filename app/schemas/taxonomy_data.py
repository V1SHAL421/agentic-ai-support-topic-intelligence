from typing import Literal
from pydantic import BaseModel, confloat

class TaxonomyData(BaseModel):
    primary_to_secondary_data: dict[str, list[str]]
    secondary_to_tertiary_data: dict[str, list[str]]

class TaxonomyOutput(BaseModel):
    primary_topic: str
    secondary_topic: str
    tertiary_topic: str
    confidence: float