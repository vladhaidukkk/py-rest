from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class User(Base):
    __tablename__ = "users"

    username: Mapped[str] = mapped_column(unique=True, index=True)
    password: Mapped[str]
