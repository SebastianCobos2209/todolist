from fastapi import FastAPI
from routes.routes import user
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

origins = [
    "http://localhost:4200", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user)
