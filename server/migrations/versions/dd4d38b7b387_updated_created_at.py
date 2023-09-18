"""updated created_at

Revision ID: dd4d38b7b387
Revises: 42604ab44119
Create Date: 2023-09-18 23:37:59.094269

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd4d38b7b387'
down_revision = '42604ab44119'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.VARCHAR(),
               type_=sa.DateTime(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.DateTime(),
               type_=sa.VARCHAR(),
               existing_nullable=True)

    # ### end Alembic commands ###
