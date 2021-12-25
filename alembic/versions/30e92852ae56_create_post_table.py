"""create-post-table

Revision ID: 30e92852ae56
Revises:
Create Date: 2021-12-19 15:35:11.545695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "30e92852ae56"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """Creating post table"""
    op.create_table(
        "posts",
        sa.Column("id", sa.Integer(), primary_key=True, nullable=False),
        sa.Column("title", sa.String(length=255), nullable=False),
    )


def downgrade():
    """Dropping post table"""
    op.drop_table("posts")
