import asyncio
import websockets

async def main():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message_to_server = "Привет, сервер!"
        await websocket.send(message_to_server)
        # Получаем пять сообщений от сервера
        for _ in range(5):
            response = await websocket.recv()
            print(response)

if __name__ == "__main__":
    asyncio.run(main())