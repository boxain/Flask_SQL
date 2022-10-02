"""first commit

Revision ID: 19a8b4862ee0
Revises: 
Create Date: 2022-10-02 20:59:54.944667

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19a8b4862ee0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('books',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('b_name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('pwd', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=False),
    sa.Column('introduction', sa.String(length=200), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.Column('register_time', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=50), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('u_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['u_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('q_name', sa.String(length=50), nullable=False),
    sa.Column('c_id', sa.Integer(), nullable=False),
    sa.Column('is_word', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['c_id'], ['comments.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('topics',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('t_name', sa.String(length=50), nullable=False),
    sa.Column('b_id', sa.Integer(), nullable=False),
    sa.Column('q_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['b_id'], ['books.id'], ),
    sa.ForeignKeyConstraint(['q_id'], ['questions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('records',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('u_id', sa.Integer(), nullable=False),
    sa.Column('t_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['t_id'], ['topics.id'], ),
    sa.ForeignKeyConstraint(['u_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('records')
    op.drop_table('topics')
    op.drop_table('questions')
    op.drop_table('comments')
    op.drop_table('users')
    op.drop_table('books')
    # ### end Alembic commands ###
