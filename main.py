from fastapi import FastAPI
from routers.users import router as users_router

app = FastAPI(
    title="FastAPI Users CRUD",
    description="Basic CRUD API for managing users",
    version="1.0.0"
)


# Home route
@app.get("/")
def home():
    return {
        "message": "My API is working successfully!"
    }


# Health check
@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


# About route
@app.get("/about")
def about():
    return {
        "project": "FastAPI Practice",
        "status": "Running"
    }


# Register Users router
app.include_router(users_router)