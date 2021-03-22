"""Create category table

Revision ID: e98134835d2d
Revises: 
Create Date: 2021-03-22 23:10:42.019810

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e98134835d2d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'categories',
        sa.Column('ID', sa.Integer, primary_key=True, index=True),
        sa.Column('Cat_name', sa.String(50), nullable=False, index=True),
        sa.Column('Pros_ID', sa.Integer),
    )



def downgrade():
    op.drop_table('categories')
