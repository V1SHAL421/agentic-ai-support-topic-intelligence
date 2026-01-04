from pydantic import BaseModel, field_validator

from app.constants import TAXONOMY_DATA

class TaxonomyData(BaseModel):
    primary_to_secondary_data: dict[str, list[str]]
    secondary_to_tertiary_data: dict[str, list[str]]

class TaxonomyOutput(BaseModel):
    model_config = {"extra": "forbid"}

    primary_topic: str
    secondary_topic: str
    tertiary_topic: str
    confidence: float = 0.0

    @field_validator('primary_topic')
    def validate_primary_topic(cls, v):
        if v not in TAXONOMY_DATA["primary_to_secondary_data"]:
            raise ValueError(f"Invalid primary topic: {v}")
        return v
    
    @field_validator('secondary_topic')
    def validate_secondary_topic(cls, v):
        if v not in TAXONOMY_DATA["secondary_to_tertiary_data"]:
            raise ValueError(f"Invalid secondary topic: {v}")
        return v
    
    @field_validator('tertiary_topic')
    def validate_tertiary_topic(cls, v, info):
        secondary_topic = info.data.get('secondary_topic')
        if secondary_topic:
            valid_tertiaries = TAXONOMY_DATA["secondary_to_tertiary_data"].get(secondary_topic, [])
            if v not in valid_tertiaries:
                raise ValueError(f"Invalid tertiary topic: {v} for secondary topic: {secondary_topic}")
        return v

class QueryRequest(BaseModel):
    user_query: str