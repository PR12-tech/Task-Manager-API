"""create missing tables

Revision ID: 605d31f15cfd
Revises: 0bd4f19c84f5
Create Date: 2026-06-19 22:32:54.095836

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '605d31f15cfd'
down_revision: Union[str, Sequence[str], None] = '0bd4f19c84f5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
    )

    op.create_index(
        "ix_users_id",
        "users",
        ["id"]
    )

    op.create_index(
        "ix_users_username",
        "users",
        ["username"],
        unique=True
    )

    op.create_table(
        "tasks",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("task", sa.String(), nullable=False),
        sa.Column("priority", sa.String(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["users.id"]
        ),
    )

    op.create_index(
        "ix_tasks_id",
        "tasks",
        ["id"]
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index("ix_tasks_id", table_name="tasks")
    op.drop_table("tasks")

    op.drop_index("ix_users_username", table_name="users")
    op.drop_index("ix_users_id", table_name="users")
    op.drop_table("users")