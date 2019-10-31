"""add language to posts

Revision ID: 97ce8f6924ff
Revises: b6a25d9c1fc1
Create Date: 2019-10-29 11:53:31.362690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97ce8f6924ff'
down_revision = 'b6a25d9c1fc1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
