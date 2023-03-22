import logging
from abc import ABC

import aiohttp
from aiohttp import WSServerHandshakeError, client_exceptions


class ConnectServer(ABC):
    """Отвечает за установку соединения с сервером"""

    async def connect(self, host, port):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.ws_connect(f"http://{host}:{port}/ws") as ws:
                    async for message in ws:
                        if message.type == aiohttp.WSMsgType.TEXT:
                            data = message.json()
                            res = await self.command_executor(data)
                            if res:
                                logging.info(
                                    f'Result after execution of command "{data.get("command")}": "{res}"\n'
                                )

                        elif message.type == aiohttp.WSMsgType.ERROR:
                            logging.error("Connection error with server\n")
                            break
        except (client_exceptions.ClientConnectionError, WSServerHandshakeError) as e:
            logging.info("Can't connect to server")
            logging.error(e)
