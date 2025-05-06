# eda-economy

Aggregate macro economic data. Implementation is minimal and as less abstract as possible.

This script is designed to aggregate macroeconomic data from various sources, including debts, gdp, inflation, and interest rates. It uses the OpenAI API to process and summarize the data. A few dollars of llm costs to run this script.

## How to run this script

Environment variables:

```bash
export OPENAI_API_KEY=xxx
export WEB_SEARCH_MODEL="gpt-4o-mini"
export DATA_DIR="local"
```

```bash
python src/main.py
```

Output file folder:

- **Debt**  ./local/debt/japan/2024/bonds_yyyymmdd_hhmmss.json

## Core parts

### Data Models

Pydantic models are used to define the structure of the data. The models are defined in the `src/models` directory. Each model corresponds to a specific type of data, such as debt. The models determine the json output structure of LLM response.

```markdown
src/models/
├── __init__.py
├── debt.py
├── entity.py
└── news.py
```

## Development Roadmap

- [x] Add more data types (government bonds)
- [ ] Add more data types (government bond spreads - yield curve)
- [ ] Add more data types (nominal gdp)
- [ ] Add more data types (inflation)
- [ ] Add more data types (central bank interest rates)
- [ ] Add more data types (trade balance)
- [ ] Add more data types (unemployment rate)
- [ ] Add more data types (money supply)
- [ ] Add more data types (stock market index)
- [ ] Add more data types (real estate prices)
- [ ] Add more data types (consumer confidence index)
- [ ] Add more data types (business confidence index)
- [ ] Add more data types (loan tightening index: auto loans)
- [ ] Add more data types (loan tightening index: mortgage loans)
- [ ] Add more data types (loan tightening index: credit card loans)
- [ ] Add more data types (loan tightening index: student loans)
- [ ] Add more data types (loan tightening index: corporate loans)
- [ ] Add more data types (loan tightening index: commercial real estate loans)
- [ ] Add more data types (loan tightening index: small business loans)
- [ ] Add more data types (loan tightening index: consumer loans)
- [ ] Add more data types (credit card debt)
- [ ] Add more data types (mortgage debt)
- [ ] Add more data types (auto loan debt)
- [ ] Add more data types (student loan debt)
- [ ] Add more data types (credit card delinquency rate)
- [ ] Add more data types (mortgage delinquency rate)
- [ ] Add more data types (auto loan delinquency rate)
- [ ] Add more data types (student loan delinquency rate)
- [ ] Add more data types (retail sales)
- [ ] Add more data types (industrial production index)
- [ ] Add more data types (capacity utilization rate)
- [ ] Add more data types (manufacturing PMI)
- [ ] Add more data types (services PMI)
- [ ] Add more data types (construction spending)
- [ ] Add more data types (housing starts)
- [ ] Add more data types (building permits)
- [ ] Add more data types (auto sales)
- [ ] Add more data types (consumer credit)
- [ ] Add more data types (business inventories)
- [ ] Add more data types (trade-weighted exchange rate)
- [ ] Add more data types (corporate bonds)
- [ ] Add more data types (corporate bond spreads)
- [ ] Add more data types (high-yield bond spreads)
- [ ] Add more data types (investment-grade bond spreads)
- [ ] Add more data types (gold prices)
- [ ] Add more data types (oil prices)
- [ ] Add more data types (natural gas prices)
- [ ] Add more data types (copper prices)
- [ ] Add more data types (silver prices)
- [ ] Add more data types (platinum prices)
- [ ] Add more data types (palladium prices)
- [ ] Add more data types (corn prices)
- [ ] Add more data types (wheat prices)
- [ ] Add more data types (soybean prices)
- [ ] Add more data types (bread prices)
- [ ] Add more data types (rice prices)
- [ ] Add more data types (potato prices)
- [ ] Add more data types (coffee prices)
- [ ] Add more data types (sugar prices)
- [ ] Add more data types (cotton prices)
- [ ] Add more data types (orange juice prices)
- [ ] Add more data types (cocoa prices)
- [ ] Add more data types (pork prices)
- [ ] Add more data types (beef prices)
- [ ] Add more data types (chicken prices)
- [ ] Add more data types (fish prices)
- [ ] Add more data types (egg prices)
- [ ] Add more data types (milk prices)
- [ ] Add more data types (Big Mac index)

## OpenAI models options

Per 1M i/o tokens

<https://platform.openai.com/docs/pricing>

- gpt-4.1-mini, gpt-4.1-mini-2025-04-14, $0.40/$1.60
- gpt-4o-mini, gpt-4o-mini-2024-07-18, $0.15/$0.60
- gpt-4.1, gpt-4.1-2025-04-14, $2.00/$8.00
- gpt-4o, gpt-4o-2024-08-06, $2.50/$10.00
