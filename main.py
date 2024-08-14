from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from auth import getToken

app = FastAPI()

# CORS SUPPORT
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

@app.get("/")
async def root():
    return "supporting server for thumbs"


@app.get("/auth")
async def auth():
    token = getToken()
    return token

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app)