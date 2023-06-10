import uvicorn
from dotenv.main import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    uvicorn.run("app.app:app", host="0.0.0.0", log_level="info")
