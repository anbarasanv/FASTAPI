"""create-relationship-users-posts

Revision ID: 12d5552f3801
Revises: 2c0fda5facc4
Create Date: 2021-12-19 15:50:50.432152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "12d5552f3801"
down_revision = "2c0fda5facc4"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        "post_users_fkey",
        source_table="posts",
        referent_table="users",
        local_cols=["owner_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )


def downgrade():
    op.drop_constraint("post_users_fkey", table_name="posts", type_="foreignkey")
    op.drop_column("posts", "owner_id")
