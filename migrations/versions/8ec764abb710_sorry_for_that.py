"""sorry for that

Revision ID: 8ec764abb710
Revises: 1996f5d83f58
Create Date: 2018-09-06 09:10:19.821785

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ec764abb710'
down_revision = '1996f5d83f58'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('activity', sa.Column('preminutes_str', sa.String(length=140), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('activity', 'preminutes_str')
    # ### end Alembic commands ###
