from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
from app.routers import auth, trips
from app.models import user, trip

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Wanderlog API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(trips.router)


@app.get("/")
def root():
    return {"message": "Wanderlog API is running"}