"""empty message

Revision ID: fe3dfb54c626
Revises: 
Create Date: 2020-01-16 14:31:07.971727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fe3dfb54c626'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=128), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('calorietarget',
    sa.Column('ctid', sa.Integer(), nullable=False),
    sa.Column('uid', sa.String(length=64), nullable=True),
    sa.Column('dtstarted', sa.String(length=40), nullable=True),
    sa.Column('dtended', sa.String(length=40), nullable=True),
    sa.Column('target', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['uid'], ['user.username'], ),
    sa.PrimaryKeyConstraint('ctid')
    )
    op.create_table('exercisetype',
    sa.Column('tid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('mets', sa.Float(), nullable=True),
    sa.Column('serv_name', sa.String(length=64), nullable=True),
    sa.Column('calories', sa.Integer(), nullable=True),
    sa.Column('caloriesperweight', sa.Integer(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['uid'], ['user.uid'], ),
    sa.PrimaryKeyConstraint('tid')
    )
    op.create_table('foodtype',
    sa.Column('ftid', sa.Integer(), nullable=False),
    sa.Column('food_name', sa.String(length=64), nullable=True),
    sa.Column('color', sa.String(length=10), nullable=True),
    sa.Column('serv_name', sa.String(length=64), nullable=True),
    sa.Column('protein_amt', sa.Integer(), nullable=True),
    sa.Column('carb_amt', sa.Integer(), nullable=True),
    sa.Column('fat_amt', sa.Integer(), nullable=True),
    sa.Column('calories', sa.Integer(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['uid'], ['user.uid'], ),
    sa.PrimaryKeyConstraint('ftid')
    )
    op.create_table('meal',
    sa.Column('mid', sa.Integer(), nullable=False),
    sa.Column('ts_created', sa.Integer(), nullable=True),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('details', sa.String(length=300), nullable=True),
    sa.Column('weightval', sa.Integer(), nullable=True),
    sa.Column('timeoffset', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['uid'], ['user.uid'], ),
    sa.PrimaryKeyConstraint('mid')
    )
    op.create_table('exerciseelement',
    sa.Column('eid', sa.Integer(), nullable=False),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('ts_created', sa.Integer(), nullable=True),
    sa.Column('length', sa.Integer(), nullable=True),
    sa.Column('etid', sa.Integer(), nullable=True),
    sa.Column('calsburned', sa.Integer(), nullable=True),
    sa.Column('previous_changes', sa.Boolean(), nullable=True),
    sa.Column('mealid', sa.Integer(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('ename', sa.String(length=40), nullable=True),
    sa.ForeignKeyConstraint(['etid'], ['exercisetype.tid'], ),
    sa.ForeignKeyConstraint(['mealid'], ['meal.mid'], ),
    sa.ForeignKeyConstraint(['uid'], ['user.uid'], ),
    sa.PrimaryKeyConstraint('eid')
    )
    op.create_table('foodelement',
    sa.Column('elementid', sa.Integer(), nullable=False),
    sa.Column('foodtypeid', sa.Integer(), nullable=True),
    sa.Column('servingsize', sa.Float(), nullable=True),
    sa.Column('userid', sa.String(length=64), nullable=True),
    sa.Column('color', sa.String(length=10), nullable=True),
    sa.Column('timestamp', sa.Integer(), nullable=True),
    sa.Column('carb_amt', sa.Integer(), nullable=True),
    sa.Column('protein_amt', sa.Integer(), nullable=True),
    sa.Column('fat_amt', sa.Integer(), nullable=True),
    sa.Column('calories', sa.Integer(), nullable=True),
    sa.Column('food_name', sa.String(length=64), nullable=True),
    sa.Column('previous_changes', sa.Boolean(), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.Column('mealid', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['foodtypeid'], ['foodtype.ftid'], ),
    sa.ForeignKeyConstraint(['mealid'], ['meal.mid'], ),
    sa.ForeignKeyConstraint(['userid'], ['user.username'], ),
    sa.PrimaryKeyConstraint('elementid')
    )
    op.create_table('weightelement',
    sa.Column('weightid', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('ts_created', sa.Integer(), nullable=True),
    sa.Column('uid', sa.String(length=64), nullable=True),
    sa.Column('mealid', sa.Integer(), nullable=True),
    sa.Column('weight', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['mealid'], ['meal.mid'], ),
    sa.ForeignKeyConstraint(['uid'], ['user.username'], ),
    sa.PrimaryKeyConstraint('weightid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weightelement')
    op.drop_table('foodelement')
    op.drop_table('exerciseelement')
    op.drop_table('meal')
    op.drop_table('foodtype')
    op.drop_table('exercisetype')
    op.drop_table('calorietarget')
    op.drop_table('user')
    # ### end Alembic commands ###
