"""empty message

Revision ID: 81bc90fb70fd
Revises: bb784f3cc4fd
Create Date: 2024-10-26 13:06:00.275340

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '81bc90fb70fd'
down_revision = 'bb784f3cc4fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admins')
    # ### end Alembic commands ###
