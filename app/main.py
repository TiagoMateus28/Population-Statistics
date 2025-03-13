# main.py
from fastapi import FastAPI
from router.populatio_router import router

app = FastAPI()

# Include the population router
app.include_router(router)
