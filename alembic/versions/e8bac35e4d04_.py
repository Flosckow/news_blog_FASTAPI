"""empty message

Revision ID: e8bac35e4d04
Revises: 11fb50abf4b1
Create Date: 2021-04-10 21:39:55.310017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8bac35e4d04'
down_revision = '11fb50abf4b1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('review_table',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body_r', sa.String(length=350), nullable=True),
    sa.Column('comment_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['users_table.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['comment_id'], ['comments_table.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_review_table_id'), 'review_table', ['id'], unique=False)
    op.add_column('comments_table', sa.Column('date', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('comments_table', 'date')
    op.drop_index(op.f('ix_review_table_id'), table_name='review_table')
    op.drop_table('review_table')
    # ### end Alembic commands ###