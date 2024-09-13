import aiohttp


async def get_status_code(url) -> int:
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                return response.status
        except aiohttp.ClientError as e:
            return 0


