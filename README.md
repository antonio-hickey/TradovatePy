# TradovatePy
Python wrapper for the Tradovate API

### Installation
```
pip install TradovatePy==0.1
```

### Example

Get the current positions you have open.

*NOTE: You need to replace values below with your info*

```python
import asyncio
from TradovatePy.models.session import Session
from TradovatePy.positions import Positions

if __name__ == "__main__":
    session = Session(
        "LIVE", 
        "YOUR_USERNAME", 
        "YOUR_PASSWORD", 
        "YOUR_SECRET_KEY", 
        "YOUR_DEVICE_ID", 
        "YOUR_APP_VERSION", 
        "YOUR_APP_ID", 
        123, # YOUR CID
    )
    print(
        asyncio.run(Positions(session).position_list())
    )
```
