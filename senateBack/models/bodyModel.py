from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime,LargeBinary
from .meta import Base
import datetime

class Body(Base):
    __tablename__ = "body"

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    title = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    contact = Column(String(50), nullable=False)
    image = Column(LargeBinary, nullable=False)

    type_of_body = Column(String(20), nullable=False)
    
    created_on = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)