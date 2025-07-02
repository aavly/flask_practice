from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    ingredients = Column(Text, nullable=False)
    instructions = Column(Text, nullable=False)

    # this method is used for debugging and logging
    def __repr__(self):
        return f"<Recipe(id={self.id}, title='{self.title}')>"