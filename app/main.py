from fastapi import FastAPI
from .database import Base, engine
from .routers import router

# Initialize FastAPI
app = FastAPI()

# Initialize Database's Table
<<<<<<< HEAD
#Base.metadata.create_all(bind=engine)
=======
Base.metadata.create_all(bind=engine)
>>>>>>> 617/main

# Register Router
app.include_router(router=router, prefix="/api", tags=["todos"])