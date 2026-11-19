"""Entry point — run the OpenAI-compatible DeepSeek server.

    python app.py            # serves on http://localhost:8000

On first use (no saved session), run `python -m deepseek.auth` once to sign in
in a visible browser. The server defaults to headless/session reuse and will
not pop open Chrome automatically. Set DEEPSEEK_PROFILE_DIR to reuse a
persistent signed-in Chrome profile.
"""

import os

import uvicorn
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    uvicorn.run(
        "server.api:app",
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "8000")),
        reload=False,
    )
