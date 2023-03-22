import argparse
import asyncio
import logging

from with_aiohttp import Lighter


async def main() -> None:

    lighter = Lighter()
    await lighter.connect(args.host, args.port)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", default="127.0.0.1", help="host to run server on")
    parser.add_argument("--port", default=9999, help="port to run server on")
    args = parser.parse_args()
    logging.info(f"Connecting to {args.host}:{args.port}\n")
    asyncio.run(main())
