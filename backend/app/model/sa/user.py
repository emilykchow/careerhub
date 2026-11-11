class Users(Base):
    """Example database model mapping to a real PostgreSQL table."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True, nullable=False)
    full_name: Mapped[str | None] = mapped_column(nullable=True)
