"""empty message

Revision ID: 518e134463fa
Revises: 15bc4aa0d87f
Create Date: 2024-06-13 22:22:40.082950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '518e134463fa'
down_revision = '15bc4aa0d87f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(length=250), nullable=True))
        batch_op.add_column(sa.Column('name2', sa.String(length=250), nullable=True))
        batch_op.add_column(sa.Column('age', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('age')
        batch_op.drop_column('name2')
        batch_op.drop_column('name')

    # ### end Alembic commands ###
