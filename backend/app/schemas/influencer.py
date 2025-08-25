from pydantic import BaseModel

class InfluencerBase(BaseModel):
    handle: str
    platform: str

class InfluencerCreate(InfluencerBase):
    pass

class Influencer(InfluencerBase):
    id: int

    class Config:
        orm_mode = True