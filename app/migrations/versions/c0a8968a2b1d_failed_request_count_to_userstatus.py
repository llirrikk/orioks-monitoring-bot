"""failed_request_count to UserStatus

Revision ID: c0a8968a2b1d
Revises: e09d97658b84
Create Date: 2022-09-13 13:20:48.446180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0a8968a2b1d'
down_revision = 'e09d97658b84'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        'user_status',
        sa.Column(
            'failed_request_count',
            sa.Integer(),
            nullable=False,
            server_default='0',
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_status', 'failed_request_count')
    # ### end Alembic commands ###
