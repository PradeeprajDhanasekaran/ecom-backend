"""Initial migration.

Revision ID: 921c1c9be3d9
Revises: 
Create Date: 2023-03-03 16:39:45.362536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '921c1c9be3d9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=26), nullable=False),
    sa.Column('last_name', sa.String(length=26), nullable=False),
    sa.Column('mobile', sa.String(length=26), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=26), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
