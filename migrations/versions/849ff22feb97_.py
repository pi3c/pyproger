"""empty message

Revision ID: 849ff22feb97
Revises: 68537cc1688c
Create Date: 2023-10-23 08:34:08.251453

"""
from alembic import op
import sqlalchemy as sa
import flask_security


# revision identifiers, used by Alembic.
revision = '849ff22feb97'
down_revision = '68537cc1688c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('footer_icons', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('page', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('header_description', sa.Text(), nullable=True))
        batch_op.create_unique_constraint(None, ['id'])

    with op.batch_alter_table('site_headers', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('site_headers', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('header_description')

    with op.batch_alter_table('page', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('footer_icons', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    # ### end Alembic commands ###
