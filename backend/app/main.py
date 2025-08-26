from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from app.api.v1.api import api_router
from app.core.config import settings
from app.services.scheduler import start_background_scheduler
from app.database import init_db

# Define the allowed origins
origins = [
    "http://localhost:3000",
    "https://<YOUR_RENDER_FRONTEND_URL>",  # Replace this with your actual frontend URL
]

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run on startup
    print("Starting up the application...")
    init_db()  # Initialize the database and tables
    start_background_scheduler()
    yield
    # Code to run on shutdown
    print("Shutting down the application...")


app = FastAPI(
    title="NichePulse AI",
    lifespan=lifespan
)

# Set up CORS (Cross-Origin Resource Sharing)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the NichePulse AI API"}