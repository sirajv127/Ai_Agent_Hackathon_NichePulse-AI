from pydantic import BaseModel

class Report(BaseModel):
    id: int
    date_range: str
    generated_brief: str

    class Config:
        orm_mode = True