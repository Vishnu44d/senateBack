from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, LargeBinary, Text
from sqlalchemy.orm import relationship
from .meta import Base
from flask_bcrypt import Bcrypt
import datetime

class Societies(Base):
    __tablename__ = "soc"

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    society_name = Column(String(50), nullable=False)
    contact_person_name = Column(String(50), nullable=False)
    phone = Column(String(15), nullable=False)
    email = Column(String(20), nullable=False)
    content = Column(Text, nullable=False)
    image = Column(LargeBinary, nullable=False)
    
    created_on = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)