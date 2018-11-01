"""expanded day

Revision ID: 7c2750fe1634
Revises: be7d5a6326b1
Create Date: 2018-09-18 04:01:30.104793

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c2750fe1634'
down_revision = 'be7d5a6326b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('day', sa.Column('total_hours', sa.Integer(), nullable=True))
    op.add_column('day', sa.Column('total_minutes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('day', 'total_minutes')
    op.drop_column('day', 'total_hours')
    # ### end Alembic commands ###
