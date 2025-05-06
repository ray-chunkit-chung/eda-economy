from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Dict, Any
import uvicorn

app = FastAPI()


########################################################################
# This is a placeholder for the actual tool registry.


# Input arguments for the tool must be defined as Pydantic models.
class GetWeatherArgs(BaseModel):
    city: str


class WeatherResponse(BaseModel):
    city: str
    temperature: str
    condition: str
    longitude: float = None
    latitude: float = None


# Tool must be defined as a function with Pydantic model as i/o arguments.
def get_weather(args: GetWeatherArgs) -> Dict[str, Any]:
    # Simulated logic (normally you’d call a weather API)

    result = WeatherResponse(city=args.city, temperature="25°C", condition="Sunny")
    return result


def get_dummy1(args: GetWeatherArgs) -> Dict[str, Any]:
    result = WeatherResponse(city=args.city, temperature="25°C", condition="Sunny")
    return result


def get_dummy2(args: GetWeatherArgs) -> Dict[str, Any]:
    result = WeatherResponse(city=args.city, temperature="25°C", condition="Sunny")
    return result


def get_dummy3(args: GetWeatherArgs) -> Dict[str, Any]:
    result = WeatherResponse(city=args.city, temperature="25°C", condition="Sunny")
    return result


tool_registry = {
    "get_weather": {"function": get_weather, "model": GetWeatherArgs},
    "get_dummy1": {"function": get_dummy1, "model": GetWeatherArgs},
    "get_dummy2": {"function": get_dummy2, "model": GetWeatherArgs},
    "get_dummy3": {"function": get_dummy3, "model": GetWeatherArgs},
}
# End of Placeholder for the actual tool registry.
########################################################################


class ToolCall(BaseModel):
    name: str
    arguments: Dict[str, Any]


class ToolRequest(BaseModel):
    tool_call: ToolCall


@app.get("/")
async def root():
    return {
        "message": "Welcome to the Tool API! Please check http://localhost:8000/docs for the API documentation."
    }


@app.post("/mcp/v1/tool_call")
async def handle_tool_call(request: ToolRequest):
    tool_name = request.tool_call.name
    args = request.tool_call.arguments

    if tool_name not in tool_registry:
        return {"error": f"Tool '{tool_name}' not found."}

    # Tool to call
    tool_func = tool_registry[tool_name]["function"]
    # Pydantic model of argument of the tool
    tool_model = tool_registry[tool_name]["model"]

    try:
        result = tool_func(tool_model(**args))
    except Exception as e:
        return {"error": f"Error while executing tool '{tool_name}': {str(e)}"}
        # raise RuntimeError(f"Error while executing tool '{tool_name}': {str(e)}")

    return {"tool_response": {"name": tool_name, "output": result}}


def create_app():
    return app


if __name__ == "__main__":
    uvicorn.run("app:create_app", host="0.0.0.0", port=8000, reload=True, factory=True)
