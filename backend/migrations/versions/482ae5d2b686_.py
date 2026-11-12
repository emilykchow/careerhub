"""Set up users and job applications tables

Revision ID: 482ae5d2b686
Revises:
Create Date: 2026-11-11 16:43:28.439456

"""

from collections.abc import Sequence

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "482ae5d2b686"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("auth0_id", sa.String, nullable=False),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("email", sa.String(50), unique=True, nullable=False),
        sa.Column("email_verified", sa.Boolean, nullable=False),
        sa.Column("password", sa.String(50), nullable=False),
        sa.Column("picture", sa.String(100), nullable=False),
    )
    op.create_table(
        "job_applications",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("user_id", sa.Integer, sa.ForeignKey("users.id"), nullable=False),
        sa.Column("job_id", sa.Integer, nullable=False),
        sa.Column("platform", sa.String(150), nullable=False),
        sa.Column("job_title", sa.String(50), nullable=False),
        sa.Column("company_name", sa.String(50), nullable=False),
        sa.Column("salary", sa.Float, nullable=True),
        sa.Column("location", sa.String(100), nullable=True),
        sa.Column("application_date", sa.Date, nullable=False),
        sa.Column("status", sa.String(20), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("users")
    op.drop_table("job_applications")
