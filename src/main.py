import os
from pathlib import Path
from typing import Optional, Dict, Any, TypedDict, List

from dotenv import load_dotenv

from utils.chat_completions import get_web_search_response
from utils.save_json import save_json_local
from models.test import News
from models.debt import Bonds, GovBonds

# Load environment variables from .env file
load_dotenv()
OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
WEB_SEARCH_MODEL: str = os.getenv("WEB_SEARCH_MODEL", "gpt-4o-mini")
# WEB_SEARCH_MODEL = os.getenv("WEB_SEARCH_MODEL", "gpt-4.1-mini")
DATA_DIR: str = os.getenv("DATA_DIR", "local")


def get_news_today() -> None:
    """
    Save today's news data to JSON file
    """
    response: Dict[str, Any] = get_web_search_response(
        api_key=OPENAI_API_KEY,
        llm_model=WEB_SEARCH_MODEL,
        input_text="What was a positive news story from today?",
        response_model=News,
    )
    _ = save_json_local(response, Path(DATA_DIR) / "test", "news")


def get_bond_info(country: str, year: int) -> Dict[str, Any]:

    # Step1: Get bond names for a specific country and year
    question = f"What bonds {country} has issued in {year}?"
    result: Dict[str, List[str]] = get_web_search_response(
        api_key=OPENAI_API_KEY,
        llm_model=WEB_SEARCH_MODEL,
        input_text=question,
        response_model=Bonds,
    )

    # Step2: Get detailed information about each bond. Separate into steps to avoid max tokens error
    bonds: List[dict] = []
    for bond_name in result.get("bond_names", []):
        question = f"""
            Please explain the following information about {bond_name} of {country} issued in {year}:
            - descriptions (str): A description of the bond.
            - issuance_volume (float): The total amount issued for the bond.
            - currency (str): The currency in which the bond is issued.
            - bond_yields (list[dict]): A dictionary mapping maturity dates to bond yields.
            - major_investors (list[str]): A list of major investors in the bond.
            - url (list[str]): List of URLs where the bond information can be found.
        """
        bond_info: Dict[str, Any] = get_web_search_response(
            api_key=OPENAI_API_KEY,
            llm_model=WEB_SEARCH_MODEL,
            input_text=question,
            response_model=GovBonds,
        )
        bond_info["bond_name"] = bond_name
        bonds.append(bond_info)

    result["bonds"] = bonds

    return result


def main() -> None:

    countries = ["China", "USA", "Japan"]
    years = [2025, 2024, 2023, 2022, 2021]

    for country in countries:
        for year in years:
            print(f"Processing {country} {year}...")
            # Get bond information for the country and year
            result = get_bond_info(country, year)
            _ = save_json_local(
                result, Path(DATA_DIR) / f"debt/{country.lower()}/{year}", "bonds"
            )


if __name__ == "__main__":
    main()
