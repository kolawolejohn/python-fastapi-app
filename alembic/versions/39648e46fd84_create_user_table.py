"""create user table

Revision ID: 39648e46fd84
Revises: 9d8482758780
Create Date: 2021-11-27 13:11:04.212305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39648e46fd84'
down_revision = '9d8482758780'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                     sa.Column('id', sa.Integer(), nullable=False),
                     sa.Column('email', sa.String(), nullable=False),
                     sa.Column('password', sa.String(), nullable=False),
                     sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),sa.PrimaryKeyConstraint('id'),
                     sa.UniqueConstraint('email')
                     )
    pass


def downgrade():
    op.drop_table('users')
    pass
