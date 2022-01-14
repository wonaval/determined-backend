"""create-workouts

Revision ID: b288aee89ab0
Revises: d0dcb13251b1
Create Date: 2022-01-10 18:51:19.410364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b288aee89ab0'
down_revision = 'd0dcb13251b1'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'workouts',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('sets', sa.Integer, nullable=False),
        sa.Column('reps', sa.Integer, nullable=False),
        sa.Column('rest', sa.Integer, nullable=False),
        sa.Column('name', sa.String),
        sa.Column('routine_id', sa.Integer),
        sa.Column('exercise_id', sa.Integer)
    )


def downgrade():
    op.drop_table('workouts')
