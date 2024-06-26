from fastapi import FastAPI
from .database import engine
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware

# models.Base.metadata.create_all(bind=engine) # alembic made this unnecessary

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # domains that talk to the api
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
        
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)