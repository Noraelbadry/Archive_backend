from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import artifacts, museums, contact, narratives

app = FastAPI(
    title="ARchive API",
    description="AI-Powered Interactive Digital Museum",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",   # ← add this (Vite's port)
        "http://localhost:3000",
    ],
    allow_credentials=True,      
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(artifacts.router)
app.include_router(museums.router)
app.include_router(contact.router)
app.include_router(narratives.router)

@app.get("/")
async def root():
    return {"message": "ARchive API is running"}