"""create zipcodes table

Revision ID: 06511b064f85
Revises:
Create Date: 2022-05-16 11:12:13.113866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06511b064f85'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'zipcodes',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('zipcode', sa.Integer, unique=True, nullable=False),
        sa.Column('risk_factor', sa.String(1), nullable=False),
    )


def downgrade():
    op.drop_table('zipcodes')
