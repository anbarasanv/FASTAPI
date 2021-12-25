"""add-columns-to-post

Revision ID: 1bb78bc36d78
Revises: 30e92852ae56
Create Date: 2021-12-19 15:39:26.381669

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1bb78bc36d78"
down_revision = "30e92852ae56"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(length=255), nullable=False))
    op.add_column(
        "posts",
        sa.Column("published", sa.Boolean(), nullable=True, server_default="TRUE"),
    )
    op.add_column(
        "posts",
        sa.Column(
            "created_at",
            sa.TIMESTAMP(timezone=True),
            nullable=True,
            server_default=sa.text("NOW()"),
        ),
    )


def downgrade():
    op.drop_column("posts", "content")
    op.drop_column("posts", "published")
    op.drop_column("posts", "created_at")
