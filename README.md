# Authorization to buff.163.com through Steam

[![pypi: package](https://img.shields.io/badge/pypi-0.0.6-blue)](https://pypi.org/project/bufflogin/)
[![Python: versions](
https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9%20%7C%203.10-blue)]()

Steam account should be registered on the buff.163.com

## Install

```bash
pip install bufflogin
```

## Usage

```python
from bufflogin import Buff
from pysteamauth.auth import Steam


async def main():
    steam = Steam(
        login='login',
        password='password',
    )
    buff = Buff(steam)
    await buff.login_to_buff()
    response: str = await buff.request('https://buff.163.com/')
```

## License

MIT