# NichePulse AI

NichePulse AI is an agent that tracks a curated list of influencers across social media, summarizes their content, and sends a trend brief every 48 hours to a brand team.

## How to Run

1.  **Prerequisites**:
    * Docker and Docker Compose must be installed.
    * You must have a Gemini API key.

2.  **Setup**:
    * Clone this repository.
    * Create a file named `.env` in the root directory.
    * Copy the contents of `.env.example` into `.env` and add your Gemini API key.

3.  **Launch the Application**:
    * Open your terminal in the project root and run the command:
        ```bash
        docker-compose up --build
        ```

4.  **Access the Application**:
    * Frontend (React App): [http://localhost:3000](http://localhost:3000)
    * Backend (FastAPI): [http://localhost:8000/docs](http://localhost:8000/docs)