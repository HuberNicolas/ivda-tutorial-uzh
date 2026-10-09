from typing import List

from pydantic import BaseModel, ConfigDict


class Company(BaseModel):
    # MongoDB documents carry an extra "_id" field that the API does not return
    model_config = ConfigDict(extra="ignore")

    id: int
    name: str
    category: str
    founding_year: int
    employees: int
    profit: List

    def to_json(self):
        return self.model_dump(mode="json", exclude_none=True)
