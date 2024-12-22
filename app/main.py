from fastapi import FastAPI
from .routers import sensor_data
from .mqtt import client as mqtt_client

app = FastAPI()

app.include_router(sensor_data.router)

@app.on_event("startup")
async def startup_event():
    mqtt_client.loop_start()

@app.on_event("shutdown")
async def shutdown_event():
    mqtt_client.loop_stop()
