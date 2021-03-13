import asyncio
import json
import logging
import websockets

logging.basicConfig()

USERS = set()


async def notify_users(message):
    if USERS:
        for id, user in enumerate(USERS):
            print('send message to %s:%s' % user.remote_address)
            await user.send(message)


async def register(websocket):
    print('client %s:%s connected' % websocket.remote_address)
    USERS.add(websocket)


async def unregister(websocket):
    print('client %s:%s disconnected' % websocket.remote_address)
    USERS.remove(websocket)


async def handle_messages(websocket, path):
    clientRole = 'web'
    try:
        async for data in websocket:
            json_payload = json.loads(data)
            print(json_payload)
            print(json_payload['action'])

            clientRole = 'worker' if json_payload['action'] == 'update_valutes' else 'web'

            if json_payload['action'] == 'connected':  # response to client
                await register(websocket)
            elif json_payload['action'] == 'update_valutes':  # response to worker
                response = json.dumps({'type': 'confirmation', 'status': 'received'})
                await websocket.send(response)
                print(f"> {response}")

                # response to clients
                await notify_users(json.dumps({
                    'type': 'notify_valutes_updated',
                    'data': json_payload['data']
                }))
            else:
                logging.error("unsupported event: {}", data)
    finally:
        if clientRole == 'web':
            await unregister(websocket)


HOST = "127.0.0.1"
PORT = 8765
print('websocket listening on %s:%s' % (HOST, PORT,))
start_server = websockets.serve(handle_messages, HOST, PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
