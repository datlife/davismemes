"""init tables

Revision ID: e4bb574d80c0
Revises: 
Create Date: 2018-11-30 10:17:39.858571

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4bb574d80c0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reddit_meme',
    sa.Column('id', sa.String(length=10), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=True),
    sa.Column('votes', sa.Integer(), nullable=True),
    sa.Column('upvote_ratio', sa.Float(), nullable=True),
    sa.Column('hotness', sa.Float(precision=15, asdecimal=6), nullable=True),
    sa.Column('funny_score', sa.Float(precision=2, asdecimal=1), nullable=True),
    sa.Column('updated', sa.DateTime(), nullable=False),
    sa.Column('created_utc', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('url')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reddit_meme')
    # ### end Alembic commands ###
