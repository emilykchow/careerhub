from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    The base class used to inherit from for creating database tables.
    Uses modern SQLAlchemy 2.0 Explicit Mapped Types.
    """
