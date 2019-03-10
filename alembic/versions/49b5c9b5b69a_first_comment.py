"""first comment

Revision ID: 49b5c9b5b69a
Revises: 
Create Date: 2019-03-10 17:18:14.622081

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49b5c9b5b69a'
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
    pass
