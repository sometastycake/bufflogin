# Authorization to buff.163.com through Steam

[![pypi: package](https://img.shields.io/badge/pypi-0.0.2-blue)](https://pypi.org/project/bufflogin/)
[![Imports: isort](https://img.shields.io/badge/imports-isort-success)](https://pycqa.github.io/isort/)
[![Linter: flake8](https://img.shields.io/badge/linter-flake8-success)](https://github.com/PyCQA/flake8)
[![Mypy: checked](https://img.shields.io/badge/mypy-checked-success)](https://github.com/python/mypy)
[![Python: versions](
https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)]()

Steam account must be registered on the buff.163.com

# Install

```bash
pip install bufflogin
```

# Usage

```python
import asyncio

from bufflogin import Buff
from pysteamauth.auth import Steam


async def main():
    steam = Steam(
        login='login',
        password='password',
        steamid=123456789,
    )
    buff = Buff(steam)
    await buff.login_to_buff()
    await buff.request('https://buff.163.com/api/market/goods/bill_order?game=csgo&goods_id=200')


if __name__ == '__main__':
    asyncio.run(main())
```
