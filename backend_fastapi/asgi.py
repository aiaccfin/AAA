import os
import uvicorn
from pathlib import Path
from app import main
from app.config import settings

api = main.create_app(settings)

def get_ssl_config():
    cert_dir = "/etc/letsencrypt/live/xai34130.ddns-ip.net"
    cert_file = Path(cert_dir) / "fullchain.pem"
    key_file = Path(cert_dir) / "privkey.pem"
    
    if cert_file.exists() and key_file.exists():
        return {
            "ssl_certfile": str(cert_file),
            "ssl_keyfile": str(key_file),
        }
    return {}

if __name__ == "__main__":
    uvicorn.run(
        "asgi:api",
        host="0.0.0.0",
        port=8080,
        reload=True,
        **get_ssl_config()
    )


# import uvicorn

# from app import main
# from app.config import settings

# api = main.create_app(settings)

# if __name__ == "__main__":
#     uvicorn.run("asgi:api", host="0.0.0.0", port=8080, reload=True)
