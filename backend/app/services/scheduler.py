import schedule
import time
import threading
from app.services import data_collector, ai_processor

# In-memory "database" for demonstration purposes
# In a real app, this would be fetched from a database (e.g., PostgreSQL, MongoDB)
tracked_influencers = [
    {"platform": "YouTube", "handle": "youtube.com/@mkbhd"},
    {"platform": "Instagram", "handle": "@nasa"},
    {"platform": "LinkedIn", "handle": "linkedin.com/in/satyanadella"},
]

def generate_and_save_report():
    """
    The main job that the scheduler will run.
    """
    print("Scheduler running: Starting content collection...")
    
    # 1. Collect content from all tracked sources
    content_list = data_collector.collect_all_content(tracked_influencers)
    
    if not content_list:
        print("Scheduler: No new content found. Skipping report generation.")
        return
        
    print(f"Scheduler: Collected {len(content_list)} pieces of content. Generating brief...")
    
    # 2. Generate the trend brief using the AI service
    brief = ai_processor.generate_trend_brief(content_list)
    
    # 3. Save the report to a database or send it via notification
    # For this example, we'll just print it to the console.
    print("--- NEW TREND BRIEF GENERATED ---")
    print(brief)
    print("---------------------------------")


def run_scheduler():
    """
    Configures and runs the job schedule.
    """
    # schedule.every(48).hours.do(generate_and_save_report)
    # For demonstration, we'll run it every 1 minute.
    schedule.every(1).minutes.do(generate_and_save_report)
    
    print("Scheduler started. Will run job every 1 minute.")
    while True:
        schedule.run_pending()
        time.sleep(1)

def start_background_scheduler():
    """
    Starts the scheduler in a non-blocking background thread.
    """
    scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
    scheduler_thread.start()