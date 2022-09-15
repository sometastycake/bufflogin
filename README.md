# Authorization to buff.163.com through Steam

# Usage

```python
import asyncio

from bufflogin import Buff
from pysteamauth.auth import Steam


async def main():
    steam = Steam(
        login='login',
        password='password',
    )
    buff = Buff(steam)
    await buff.login_to_buff()
    await buff.request('https://buff.163.com/api/market/goods/bill_order?game=csgo&goods_id=200')


if __name__ == '__main__':
    asyncio.run(main())
```