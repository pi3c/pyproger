"""empty message

Revision ID: 055327bef08e
Revises: 849ff22feb97
Create Date: 2023-10-23 09:29:00.193470

"""
from alembic import op
import sqlalchemy as sa
import flask_security


# revision identifiers, used by Alembic.
revision = '055327bef08e'
down_revision = '849ff22feb97'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('page', schema=None) as batch_op:
        batch_op.add_column(sa.Column('header_description', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('page', schema=None) as batch_op:
        batch_op.drop_column('header_description')

    # ### end Alembic commands ###
