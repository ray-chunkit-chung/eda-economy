import os
import json
from typing import Optional, Dict, Any
from datetime import datetime
from pathlib import Path

from dotenv import load_dotenv

from utils.chat_completions import get_web_search_response
from models.test import News

# Load environment variables from .env file
load_dotenv()
OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
WEB_SEARCH_MODEL: str = os.getenv("WEB_SEARCH_MODEL", "gpt-4o-mini")
# WEB_SEARCH_MODEL = os.getenv("WEB_SEARCH_MODEL", "gpt-4.1-mini")
DATA_DIR: str = os.getenv("DATA_DIR", "local")


def save_json_response(data: Dict[str, Any], directory: str, data_name: str) -> None:
    """Save JSON response to a file with timestamp."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{data_name}_{timestamp}.json"
    path = Path(directory) / filename

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        # ensure_ascii=False allows Unicode characters to be written directly
        # instead of being escaped (e.g., "世界" vs "\u4e16\u754c")
        json.dump(data, f, indent=2, ensure_ascii=False)


def main() -> None:
    # Save test news data to JSON file
    response: Dict[str, Any] = get_web_search_response(
        api_key=OPENAI_API_KEY,
        model=WEB_SEARCH_MODEL,
        input_text="What was a positive news story from today?",
        response_model=News,
    )
    save_json_response(response, Path(DATA_DIR) / "test", "news")


if __name__ == "__main__":
    main()
