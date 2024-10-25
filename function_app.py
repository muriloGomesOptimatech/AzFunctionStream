import azure.functions as func
from azurefunctions.extensions.http.fastapi import Request, StreamingResponse
from time import sleep

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

def generate_sensor_data():
    """Generate real-time sensor data."""
    for i in range(50):
        # Simulate temperature and humidity readings
        temperature = 20 + i
        humidity = 50 + i
        yield f"data: {{'temperature': {temperature}, 'humidity': {humidity}}}\n\n"
        sleep(2.5)


@app.route(route="stream", methods=[func.HttpMethod.GET])
async def stream_sensor_data(req: Request) -> StreamingResponse:
    """Endpoint to stream real-time sensor data."""
    return StreamingResponse(generate_sensor_data(), media_type="text/event-stream")

