from fastapi import APIRouter, HTTPException
from typing import List
import sqlite3
from app.schemas.report import Report
from app.services import ai_processor, data_collector
from datetime import datetime, timedelta

router = APIRouter()
DATABASE_FILE = "nichepulse.db"

@router.get("/", response_model=List[Report])
def get_stored_reports():
    """
    Retrieves all stored reports from the SQLite database.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reports ORDER BY id DESC")
    reports_rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in reports_rows]

@router.post("/generate", response_model=Report)
def generate_and_store_new_report():
    """
    Generates a new trend brief, stores it in the database,
    and returns the newly created report.
    """
    print("API called: Generating a new report to store in the database...")
    
    # In a future step, this will be replaced with live data from the database
    tracked_influencers = [
        {"platform": "YouTube", "handle": "youtube.com/@mkbhd"},
        {"platform": "Instagram", "handle": "@nasa"},
    ]
    
    content_list = data_collector.collect_all_content(tracked_influencers)
    generated_text = ai_processor.generate_trend_brief(content_list)
    
    today = datetime.now()
    two_days_ago = today - timedelta(days=2)
    date_range_str = f"{two_days_ago.strftime('%B %d, %Y')} - {today.strftime('%B %d, %Y')}"
    
    new_report_id = int(today.timestamp())
    
    new_report = Report(
        id=new_report_id,
        date_range=date_range_str,
        generated_brief=generated_text
    )
    
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO reports (id, date_range, generated_brief) VALUES (?, ?, ?)",
        (new_report.id, new_report.date_range, new_report.generated_brief)
    )
    conn.commit()
    conn.close()
    
    print(f"Successfully generated and stored report with ID: {new_report.id}")
    return new_report
@router.delete("/{report_id}", status_code=204)
def delete_report(report_id: int):
    """
    Deletes a report from the SQLite database by its ID.
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    # Check if the report exists before deleting
    cursor.execute("SELECT id FROM reports WHERE id = ?", (report_id,))
    report = cursor.fetchone()
    if report is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Report not found")
        
    cursor.execute("DELETE FROM reports WHERE id = ?", (report_id,))
    conn.commit()
    conn.close()
    
    print(f"Successfully deleted report with ID: {report_id}")
    return {"ok": True} # Return a success response