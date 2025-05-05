import json
from typing import Dict, Any
from datetime import datetime
from pathlib import Path

__all__ = [
    "save_json_local",
]


def save_json_local(
    data: Dict[str, Any], directory: str | Path, data_name: str
) -> Path:
    """Save JSON response to a file with timestamp.

    Args:
        data: Dictionary containing the data to save
        directory: Directory path as string or Path object
        data_name: Base name for the output file

    Returns:
        Path object pointing to the saved file
    """
    timestamp: str = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename: str = f"{data_name}_{timestamp}.json"
    path: Path = Path(directory) / filename

    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        # ensure_ascii=False allows Unicode characters to be written directly
        # instead of being escaped (e.g., "世界" vs "\u4e16\u754c")
        json.dump(data, f, indent=2, ensure_ascii=False)

    return path
