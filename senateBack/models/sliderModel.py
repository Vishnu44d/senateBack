from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, LargeBinary
from .meta import Base
import datetime

class Slider(Base):
    __tablename__ = "slider"

    id = Column(Integer, primary_key=True, autoincrement=True)
    
    title = Column(String(50), nullable=False)
    subtitle = Column(String(500))
    image = Column(LargeBinary, nullable=False)
    
    created_on = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)