from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from datetime import datetime, timezone
import httpx
import os
import logging
import uvicorn

# Load environment variables
load_dotenv()

# Initialize app
app = FastAPI(
    title="Stage 0 Dynamic Profile API",
    description="A simple FastAPI app returning user profile + cat fact.",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

CATFACT_API_URL = "https://catfact.ninja/fact"

@app.get("/me", response_class=JSONResponse)
async def get_profile():
    """Get user profile along with a cat fact and current timestamp."""
    user_email = os.getenv("USER_EMAIL")
    user_name = os.getenv("USER_NAME")
    user_stack = os.getenv("USER_STACK")

    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(CATFACT_API_URL)
            response.raise_for_status()
            cat_fact_data = response.json()
            cat_fact = cat_fact_data.get("fact", "No cat fact available.")
    except Exception as e:
        logger.error(f"Error fetching cat fact: {e}")
        cat_fact = "Could not retrieve cat fact at this time. Try again later."

    current_timestamp = datetime.now(timezone.utc).isoformat()

    profile_data = {
        "status": "success",
        "user": {
            "name": user_name,
            "email": user_email,
            "stack": user_stack,
        },
        "fact": cat_fact,
        "timestamp": current_timestamp,
    }

    logger.info("Profile data retrieved successfully.")
    return JSONResponse(content=profile_data, headers={"Content-Type": "application/json"})



@app.get("/")
def home():
    return {"message": "Hello!"}

if __name__ == "__main__":
    
    port = int(os.environ.get("PORT", 8000))  
    uvicorn.run(app, host="0.0.0.0", port=port)