"""add user table

Revision ID: 3fe46b532b6c
Revises: 
Create Date: 2019-03-10 18:03:31.249643

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3fe46b532b6c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    user = op.create_table(
        'User',
        sa.Column('userId', sa.Integer, primary_key=True, nullable=False, autoincrement=True),
        sa.Column('userName', sa.String(100), nullable=False),
        sa.Column('password', sa.String(40), nullable=False),
    )

    op.bulk_insert(
        user,
        [
            {"userName": "Admin", "password": 'admin'},
        ]
    )


def downgrade():
    op.drop_table('User')
