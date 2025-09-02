from agents import Agent, Runner, ResponseFormat
from pydantic import BaseModel
import asyncio
from security_wrapper import secure_request_wrapper

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    condition: str
    humidity: int

agent = Agent(
    name="Weather Bot",
    instructions="Provide weather info in the requested JSON format.",
    response_format=ResponseFormat(WeatherResponse)
)

async def main():
    res = await Runner.run(agent, "What's the weather in San Francisco?")
    weather_data = res.structured_output
    print(f"City: {weather_data.city}")
    print(f"Temp: {weather_data.temperature}°F")
    print(f"Condition: {weather_data.condition}")

if __name__ == "__main__":
    asyncio.run(main())