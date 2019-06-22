"""empty message

Revision ID: 8594b73ac54b
Revises: 3d6e4d3ea208
Create Date: 2019-06-22 11:18:19.972614

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8594b73ac54b'
down_revision = '3d6e4d3ea208'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('weightelement', schema=None) as batch_op:
        batch_op.add_column(sa.Column('mealid', sa.Integer(), nullable=True))
        batch_op.create_foreign_key("fk_weightelement", 'meal', ['mealid'], ['mid'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('weightelement', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('mealid')

    # ### end Alembic commands ###