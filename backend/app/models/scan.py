from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Scan(Base):
    __tablename__ = "scans"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    target: Mapped[str] = mapped_column(
        String(255)
    )

    status: Mapped[str] = mapped_column(
        String(50),
        default="pending"
    )