"""some commit

Revision ID: fe331c329e4a
Revises: c901d4f41e69
Create Date: 2024-03-31 03:54:39.837391

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fe331c329e4a'
down_revision: Union[str, None] = 'c901d4f41e69'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
