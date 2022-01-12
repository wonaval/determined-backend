"""create-log-entry

Revision ID: 32f435fccd2e
Revises: 94e835e8242f
Create Date: 2022-01-12 12:00:39.545107

"""
from sqlalchemy.sql.expression import null
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32f435fccd2e'
down_revision = '94e835e8242f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'entries',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('sets', sa.Integer, nullable=False),
        sa.Column('reps', sa.Integer, nullable=False),
        sa.Column('weight', sa.Integer, nullable=False),
        sa.Column('log_id', sa.Integer),
        sa.Column('exercise_id', sa.Integer)
    )

def downgrade():
    op.drop_table('entries')
