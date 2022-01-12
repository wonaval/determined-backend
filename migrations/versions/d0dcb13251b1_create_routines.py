"""create-routines

Revision ID: d0dcb13251b1
Revises: 2b08df175a39
Create Date: 2022-01-10 18:41:23.453864

"""
from sqlalchemy.sql.expression import null, nullslast
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0dcb13251b1'
down_revision = '2b08df175a39'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'routines',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, unique=True, nullable=False),
        sa.Column('type', sa.String),
        sa.Column('user_id', sa.Integer),

    )


def downgrade():
    op.drop_table('routines')
