#database connection
from .database import Base
from sqlalchemy import Column, ForeignKey,Integer,String,Boolean
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String(99), nullable=False)
    password = Column(String(499), nullable=False)
    is_active = Column(Boolean, nullable=False, server_default='FALSE')
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))

class Code(Base):
    __tablename__ = "codes"
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(99), nullable=False)
    content = Column(String(9999), nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))
    user_id = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"), nullable=False)

class Vote(Base):
    __tablename__ = "votes"
    code_id = Column(Integer, ForeignKey(Code.id, ondelete="CASCADE"), primary_key = True)
    user_id = Column(Integer, ForeignKey(User.id, ondelete="CASCADE"), primary_key = True)