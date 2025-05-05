from pydantic import BaseModel, Field


class BondYield(BaseModel):
    """
    A Pydantic model representing bond yield information.

    Attributes:
        maturity (str): The date when the bond matures.
        yield_percentage (float): The yield of the bond in percentage.

    Example:
        bond_yield = BondYield(
            maturity="2025-12-31",
            yield_percentage=1.88
        )
    """

    maturity: str = Field(..., description="The date when the bond matures.")
    yield_percentage: float = Field(
        ..., description="The yield of the bond in percentage."
    )


class GovBonds(BaseModel):
    """
    A Pydantic model representing bond information.

    Attributes:
        descriptions (str): A description of the bond.
        issuance_volume (float): The total amount issued for the bond.
        currency (str): The currency in which the bond is issued.
        bond_yields (list[dict]): A dictionary mapping maturity dates to bond yields.
        major_investors (list[str]): A list of major investors in the bond.
        url (list[str]): List of URLs where the bond information can be found.
    """

    # bond_name: str = Field(..., description="The identifier or name of the bond.")
    descriptions: str = Field(..., description="A description of the bond.")
    issuance_volume: float = Field(
        ..., description="The total amount issued for the bond."
    )
    currency: str = Field(..., description="The currency in which the bond is issued.")
    bond_yields: list[BondYield] = Field(
        ...,
        description="A dictionary mapping maturity dates to bond yields.",
    )
    major_investors: list[str] = Field(
        ...,
        description="A list of major investors who buy the bond.",
    )
    url: list[str] = Field(
        ..., description="List of URLs where the bond information can be found."
    )


class Bonds(BaseModel):
    """
    A Pydantic model representing bonds issued by a country.

    Attributes:
        country (str): The country that issued the bond.
        year (int): The year the bond was issued.
        bonds (list[GovBond]): List of government bonds issued.
    """

    country: str = Field(..., description="The country that issued the bond.")
    year: int = Field(..., description="The year the bond was issued.")
    # quarter: int = Field(
    #     ..., description="The quarter of the year (1-4) when the bond was issued."
    # )
    bond_names: list[str] = Field(
        ..., description="The identifier or name of the bond."
    )
