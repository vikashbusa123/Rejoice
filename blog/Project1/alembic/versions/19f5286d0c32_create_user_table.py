"""create user table

Revision ID: 19f5286d0c32
Revises: 
Create Date: 2023-08-31 18:14:50.663732

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '19f5286d0c32'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
       'Posts',
       sa.Column('id', sa.Integer, primary_key=True,unique=True),
       sa.Column('ocation', sa.String(50), nullable=False),
       sa.Column('photo', sa.String(100)),
       sa.Column('caption',sa.String(100)),
       sa.Column('upload_time',sa.DateTime)
    )


def downgrade() -> None:
    pass
