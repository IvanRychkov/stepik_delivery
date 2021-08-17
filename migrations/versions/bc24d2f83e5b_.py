"""empty message

Revision ID: bc24d2f83e5b
Revises: 
Create Date: 2021-08-17 04:13:03.216412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc24d2f83e5b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mail', sa.String(), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('mail')
    )
    op.create_table('meals',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('picture', sa.String(), nullable=True),
    sa.Column('category_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_id'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('amount', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('mail', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['mail'], ['users.mail'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('orders_meals',
    sa.Column('meal_id', sa.Integer(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['meal_id'], ['meals.id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['orders.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders_meals')
    op.drop_table('orders')
    op.drop_table('meals')
    op.drop_table('users')
    op.drop_table('categories')
    # ### end Alembic commands ###
