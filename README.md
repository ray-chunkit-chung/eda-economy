# eda-economy

Aggregate macro economic data. Implementation is minimal and as less abstract as possible.

This script is designed to aggregate macroeconomic data from various sources, including debts, TODO: gdp, inflation, and interest rates. It uses the OpenAI API to process and summarize the data. A few dollars of llm costs to run this script.

How to run:

```bash
python src/main.py

# Output file folder: ./local/debt/japan/2024/bonds_yyyymmdd_hhmmss.json
```

environment variables:

```bash
export OPENAI_API_KEY=xxx
export WEB_SEARCH_MODEL="gpt-4o-mini"
export DATA_DIR="local"
```

## OpenAI models options

Per 1M i/o tokens

<https://platform.openai.com/docs/pricing>

- gpt-4.1-mini, gpt-4.1-mini-2025-04-14, $0.40/$1.60
- gpt-4o-mini, gpt-4o-mini-2024-07-18, $0.15/$0.60
- gpt-4.1, gpt-4.1-2025-04-14, $2.00/$8.00
- gpt-4o, gpt-4o-2024-08-06, $2.50/$10.00
