from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from . import models
from .database import engine
from .routers import products, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="TecnoNow API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(products.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"status": "ok"}