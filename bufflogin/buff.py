from typing import (
    Any,
    Dict,
    Optional,
)

import lxml.html as html
from pysteamauth.abstract import (
    CookieStorageAbstract,
    RequestStrategyAbstract,
)
from pysteamauth.auth import Steam
from pysteamauth.base import (
    BaseCookieStorage,
    BaseRequestStrategy,
)

from .exceptions import BuffLoginError
from .schemas import BuffAuthorizationStatus


class Buff:
    def __init__(
        self,
        steam: Steam,
        cookie_storage: Optional[CookieStorageAbstract] = None,
        request_strategy: Optional[RequestStrategyAbstract] = None,
    ):
        self._steam = steam
        self._requests = request_strategy if request_strategy is not None else BaseRequestStrategy()
        self._storage = cookie_storage if cookie_storage is not None else BaseCookieStorage()

    async def request(self, url: str, method: str = 'GET', **kwargs: Any) -> str:
        return await self._requests.text(
            url=url,
            method=method,
            cookies=await self._storage.get(self._steam.login, domain='buff.163.com'),
            **kwargs,
        )

    async def is_authorized(self) -> bool:
        response: str = await self.request(
            url='https://buff.163.com/api/market/goods/bill_order',
        )
        return BuffAuthorizationStatus.parse_raw(response).is_authorized()

    def parse_openid_params(self, response: str) -> Dict[str, str]:
        page = html.document_fromstring(response)
        params = {
            'action': '',
            'openid.mode': '',
            'openidparams': '',
            'nonce': '',
        }
        for key in params:
            params[key] = page.cssselect(f'input[name="{key}"]')[0].attrib['value']
        return params

    async def get_openid_params(self) -> Dict[str, str]:
        response = await self._requests.text(
            method='GET',
            url='https://buff.163.com/account/login/steam?back_url=/',
            cookies=await self._steam.cookies(),
        )
        return self.parse_openid_params(response)

    async def login_to_buff(self) -> None:
        if await self.is_authorized():
            return
        await self._steam.login_to_steam()
        await self._requests.bytes(
            method='POST',
            url='https://steamcommunity.com/openid/login',
            data=await self.get_openid_params(),
            cookies=await self._steam.cookies(),
        )
        await self._storage.set(
            login=self._steam.login,
            cookies={
                'buff.163.com': self._requests.cookies('buff.163.com'),
            },
        )
        if not await self.is_authorized():
            raise BuffLoginError(self._steam.login)
