"""add created_at column to post table

Revision ID: 19a8561ce853
Revises: ff7a0e91f8da
Create Date: 2021-11-27 13:15:45.825555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19a8561ce853'
down_revision = 'ff7a0e91f8da'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts', 'created_at')
    pass
