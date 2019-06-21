"""empty message

Revision ID: 33ef28090bb4
Revises: 998a9bc53e03
Create Date: 2019-06-14 08:49:04.553433

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33ef28090bb4'
down_revision = '998a9bc53e03'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exercisetype', schema=None) as batch_op:
        batch_op.add_column(sa.Column('calperlb', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('serv_name', sa.String(length=64), nullable=True))
        batch_op.drop_column('color')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('exercisetype', schema=None) as batch_op:
        batch_op.add_column(sa.Column('color', sa.VARCHAR(length=10), nullable=True))
        batch_op.drop_column('serv_name')
        batch_op.drop_column('calperlb')

    # ### end Alembic commands ###