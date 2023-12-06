"""Rename column in Student model

Revision ID: 9dd868a340e3
Revises: 18cb70238806
Create Date: 2023-12-06 23:58:59.453711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9dd868a340e3'
down_revision = '18cb70238806'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'scholars')

def downgrade() -> None:
    op.alter_column('students', 'scholars')
