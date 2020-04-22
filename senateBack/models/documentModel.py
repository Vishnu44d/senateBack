from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, LargeBinary
from .meta import Base
import datetime

class Document(Base):
    __tablename__ = "document"

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    title = Column(String(50), nullable=False)
    type_of_doc = Column(String(50), nullable=False)
    doc = Column(LargeBinary, nullable=False)
    
    created_on = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)