"""empty message

Revision ID: c39d71c733b2
Revises: 9d2828aa95a0
Create Date: 2017-11-08 13:02:22.154243

"""

# revision identifiers, used by Alembic.
revision = 'c39d71c733b2'
down_revision = '9d2828aa95a0'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('db_meta_data', sa.Column('version_string', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('db_meta_data', 'version_string')
    # ### end Alembic commands ###