from pydantic import BaseModel

class TaxonomyData(BaseModel):
    primary_to_secondary_data: dict[str, list[str]]
    secondary_to_tertiary_data: dict[str, list[str]]