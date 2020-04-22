from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, LargeBinary
from .meta import Base
import datetime

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, autoincrement=True)

    title = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)

    isFile = Column(Boolean, nullable=False, default=False)
    supported_doc = Column(LargeBinary)

    created_on = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)