from fastapi import APIRouter, HTTPException, status

from schemas.user import UserCreate, UserUpdate
from services import user_service


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


# Create user
@router.post("/", status_code=201)
def create_user(user: UserCreate):
    return user_service.create_user(user)


# Get all users
@router.get("/")
def get_all_users():
    return user_service.get_all_users()


# Get user by ID
@router.get("/{user_id}")
def get_user(user_id: int):
    user = user_service.get_user_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# Update user
@router.put("/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    updated_user = user_service.update_user(
        user_id,
        user
    )

    if updated_user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return updated_user


# Delete user
@router.delete("/{user_id}")
def delete_user(user_id: int):
    deleted = user_service.delete_user(user_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "message": "User deleted successfully"
    }