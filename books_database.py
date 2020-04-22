from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Books(Base):
    __tablename__ = "books"
    isbn = Column(String, primary_key = True)
    title = Column(String, nullable = True)
    author = Column(String, nullable = True)
    year = Column(String, nullable = True)

    def __init__(self, isbn, title, author, year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.year = year
        