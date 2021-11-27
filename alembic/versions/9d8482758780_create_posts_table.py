"""create posts table

Revision ID: 9d8482758780
Revises: 
Create Date: 2021-11-27 13:07:24.573835

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9d8482758780'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', 
    sa.Column('id', sa.Integer(), nullable=False, primary_key=True), 
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('content', sa.String(), nullable=False),
    sa.Column('published', sa.Boolean(), nullable=False, server_default='TRUE') )
    pass


def downgrade():
    op.drop_table('posts')
    pass