from fastapi import APIRouter
from .database import query_api, write_api

router = APIRouter()

@router.get("/sensor_data")
async def get_sensor_data():
    query = 'from(bucket:"your-bucket") |> range(start: -1h)'
    result = query_api.query(org="your-org", query=query)
    return result

@router.post("/send_command")
async def send_command(command: str):
    client.publish("your/topic", command)
    return {"status": "command sent"}
