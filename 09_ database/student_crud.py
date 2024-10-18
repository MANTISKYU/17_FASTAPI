from sqlalchemy.orm import Session
import schemas, models
from fastapi import HTTPException


def create_student(db : Session, student = schemas.StudentCreate):
    
    db_student = models.Student(
        name=student.name,
        is_active=student.is_active,
        nickname=student.nickname,
        description=student.description
    )
    
    db.add(db_student)
    db.commit()
    
    return db_student