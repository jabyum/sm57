from fastapi import FastAPI
from api.photo.photo_api import photo_router
app = FastAPI(docs_url="/")

app.include_router(photo_router)

# uvicorn main:app --reload
