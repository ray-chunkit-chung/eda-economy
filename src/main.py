import os
from pathlib import Path
from typing import Optional, Dict, Any

from dotenv import load_dotenv

from utils.chat_completions import get_web_search_response
from utils.save_json import save_json_local
from models.test import News

# Load environment variables from .env file
load_dotenv()
OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
WEB_SEARCH_MODEL: str = os.getenv("WEB_SEARCH_MODEL", "gpt-4o-mini")
# WEB_SEARCH_MODEL = os.getenv("WEB_SEARCH_MODEL", "gpt-4.1-mini")
DATA_DIR: str = os.getenv("DATA_DIR", "local")


def main() -> None:
    # Save test news data to JSON file
    response: Dict[str, Any] = get_web_search_response(
        api_key=OPENAI_API_KEY,
        model=WEB_SEARCH_MODEL,
        input_text="What was a positive news story from today?",
        response_model=News,
    )
    _ = save_json_local(response, Path(DATA_DIR) / "test", "news")


if __name__ == "__main__":
    main()
