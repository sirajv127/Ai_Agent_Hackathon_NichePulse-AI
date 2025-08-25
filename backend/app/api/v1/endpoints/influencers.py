from fastapi import APIRouter
from typing import List
import sqlite3
from app.schemas.influencer import InfluencerCreate, Influencer

router = APIRouter()
DATABASE_FILE = "nichepulse.db"

@router.post("/", response_model=Influencer)
def add_influencer(influencer: InfluencerCreate):
    """
    Adds a new influencer to the SQLite database.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO influencers (handle, platform) VALUES (?, ?)",
        (influencer.handle, influencer.platform)
    )
    new_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return Influencer(id=new_id, **influencer.dict())

@router.get("/", response_model=List[Influencer])
def get_influencers():
    """
    Retrieves all stored influencers from the SQLite database.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM influencers")
    influencers_rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in influencers_rows]