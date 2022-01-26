import asyncio
from datetime import datetime

from aiohttp import ClientSession

from app.config import URLs
from app.util.date_and_time import parse_hour


class Session:
    def __init__(self,
                 environment: str,
                 username: str,
                 password: str,
                 secret_key: str = "",
                 device_id: str = "",
                 app_version: str = "",
                 app_id: str = "",
                 cid: int = 0) -> None:
        """Session constructor."""
        self.env: str = environment
        self.username: str = username
        self.password: str = password
        self.secret_key: str = secret_key
        self.device_id: str = device_id
        self.app_version: str = app_version
        self.app_id: str = app_id
        self.cid: int = cid
        self.URL: str = URLs[self.env]
        self.CREDs: dict = self.render_credentials_payload()
        self.access_tokens: dict = asyncio.run(self.get_access_tokens())
        self.access_token: str = self.access_tokens['accessToken']
        self.market_data_access_token: str = self.access_tokens['mdAccessToken']
        self.token_expiration_time: str = self.access_tokens['expirationTime'].replace("T", " ")[:-8]
        self.headers: dict = {
            'Authorization': f'Bearer {self.access_token}',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        }

    async def __aenter__(self):
        """Enter client session."""
        self._session = ClientSession()
        return self

    async def __aexit__(self):
        """Exit client session."""
        await self._session.close()

    async def get_access_tokens(self):
        """Trade credentials for tokens."""
        await self.__aenter__()
        url = f"{self.URL}/auth/accesstokenrequest"
        async with self._session.post(url, json=self.CREDs, ssl=False) as resp:
            return await resp.json()

    async def get(self, url: str):
        """Send GET request to a spicified url."""
        await self.__aenter__()
        url = f"{self.URL + url}"
        async with self._session.get(url, headers=self.headers, ssl=False) as resp:
            return await resp.json()

    async def post(self, url: str, payload: dict):
        """Send POST request to a specified url with a specified payload."""
        await self.__aenter__()
        url = f"{self.URL + url}"
        async with self._session.post(url, headers=self.headers, json=payload, ssl=False) as resp:
            return await resp.json()

    def render_credentials_payload(self) -> dict:
        """Create credentials payload."""
        payload = {
            "name": self.username,
            "password": self.password,
        }

        if self.secret_key != "":
            payload['sec'] = self.secret_key
        if self.device_id != "":
            payload['deviceId'] = self.device_id
        if self.app_id != "":
            payload['appId'] = self.app_id
        if self.app_version != "":
            payload['appVersion'] = self.app_version
        if self.cid != 0:
            payload['cid'] = str(self.cid)

        return payload

    async def expiration_check(self) -> bool:
        """Check if tokens are close to expiration."""
        right_now = str(datetime.now())[:-10]
        hours = parse_hour([right_now, self.token_expiration_time])

        if hours[right_now] == hours[self.token_expiration_time]:
            return True
        return False
