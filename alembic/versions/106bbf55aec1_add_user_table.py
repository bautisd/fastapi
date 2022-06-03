"""add user table

Revision ID: 106bbf55aec1
Revises: a76a12068a7d
Create Date: 2022-06-02 18:59:52.111563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '106bbf55aec1'
down_revision = 'a76a12068a7d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
