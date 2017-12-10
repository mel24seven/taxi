"""empty message

Revision ID: 4b52b975d520
Revises: ce377bda6037
Create Date: 2017-12-10 20:09:01.552517

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4b52b975d520'
down_revision = 'ce377bda6037'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.String(), nullable=False),
    sa.Column('driver_id', sa.String(), nullable=True),
    sa.Column('req_status', sa.Enum('COMPLETED', 'ONGOING', 'WAITING', name='reqstatus'), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('requests')
    # ### end Alembic commands ###