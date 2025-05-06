# API endpoints

## Example

Payload. Must contain request.tool_call.name and arguments:

```json
{
  "tool_call": {
    "name": "get_weather",
    "arguments": {
      "city": "Tokyo"
    }
  }
}
```

```json
{
  "tool_call": {
    "name": "get_weather",
    "arguments": {
      "city": "Tokyo"
    }
  }
}
```

Request:

```bash
curl -X 'POST' \
  'http://localhost:8000/mcp/tool_call' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "tool_call": {
    "name": "get_weather",
    "arguments": {
      "city": "Tokyo"
    }
  }
}'
```

Response:

```json
{
  "tool_response": {
    "name": "get_weather",
    "output": {
      "city": "Tokyo",
      "temperature": "20°C",
      "condition": "Sunny"
    }
  }
}
```

## Tool Call list
