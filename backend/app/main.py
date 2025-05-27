from fastapi import FastAPI
from app.routers import user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "Welcome to FlexiServe API"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:3000"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
