"""Renaming students to scholars

Revision ID: 18cb70238806
Revises: 791279dd0760
Create Date: 2023-12-06 23:24:49.826414

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18cb70238806'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
