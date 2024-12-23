from fastapi import FastAPI
from .database import Base, engine
from .routers import router

# Initialize FastAPI
app = FastAPI()

# Initialize Database's Table
<<<<<<< HEAD
<<<<<<< HEAD
#Base.metadata.create_all(bind=engine)
=======
Base.metadata.create_all(bind=engine)
>>>>>>> 617/main
=======
#Base.metadata.create_all(bind=engine)
>>>>>>> d71486fedfd6640980c7d05d850b95895c95091d

# Register Router
app.include_router(router=router, prefix="/api", tags=["todos"])