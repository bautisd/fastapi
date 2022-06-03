"""add content colum to post table

Revision ID: a76a12068a7d
Revises: 3862526b6389
Create Date: 2022-06-02 18:54:38.079764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a76a12068a7d'
down_revision = '3862526b6389'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("posts", sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
