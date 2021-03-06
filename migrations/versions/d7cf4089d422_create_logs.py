"""create-logs

Revision ID: d7cf4089d422
Revises: b288aee89ab0
Create Date: 2022-01-10 18:51:33.329782

"""
from sqlalchemy.sql.expression import null
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd7cf4089d422'
down_revision = 'b288aee89ab0'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'logs',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('date', sa.Date),
        sa.Column('name', sa.String),
        sa.Column('user_id', sa.Integer)
    )


def downgrade():
    op.drop_table('logs')
