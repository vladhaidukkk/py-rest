from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

metadata = MetaData(
    naming_convention={
        "all_column_names": lambda constraint, _table: "_".join(
            [column.name for column in constraint.columns.values()]  # type: ignore[attr-defined]
        ),
        "ix": "ix_%(table_name)s_%(all_column_names)s",
        "uq": "uq_%(table_name)s_%(all_column_names)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(all_column_names)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s",
    }
)


class Base(DeclarativeBase):
    metadata = metadata

    id: Mapped[int] = mapped_column(primary_key=True)
