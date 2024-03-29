"""empty message

Revision ID: 4169b6ddd503
Revises: 614ed1ac1b56
Create Date: 2023-04-06 16:46:42.036031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4169b6ddd503'
down_revision = '614ed1ac1b56'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('instructors', sa.Column('is_chair', sa.Boolean(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('instructors', 'is_chair')
    # ### end Alembic commands ###
