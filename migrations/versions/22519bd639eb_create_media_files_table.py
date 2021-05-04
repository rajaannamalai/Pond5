"""create media files table

Revision ID: 22519bd639eb
Revises: 
Create Date: 2021-05-03 13:04:18.528254

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '22519bd639eb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    media_file = op.create_table(
        'media_file',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('file_name', sa.String(250), nullable=False),
        sa.Column('media_type', sa.String(50), nullable=False),
        sa.Column('created_dt', sa.DateTime, nullable=False, server_default=sa.func.now()),
        sa.Column('updated_dt', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now()))


def downgrade():
    op.drop_table('media_file')

