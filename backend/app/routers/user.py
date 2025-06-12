from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.database import SessionLocal
from app import models
from app.schemas import user as schemas

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=dict)
def create_user(user_req: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = models.user.User(name=user_req.name, email=user_req.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return {"message": "User created successfully", "user": db_user}


@router.get("/", response_model=list[schemas.UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(models.user.User).all()
