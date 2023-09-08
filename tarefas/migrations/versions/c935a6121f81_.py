"""empty message

Revision ID: c935a6121f81
Revises: 
Create Date: 2023-09-06 20:30:31.275764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c935a6121f81'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('estado',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('status', sa.String(length=55), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('senha', sa.String(length=150), nullable=True),
    sa.Column('nome', sa.String(length=150), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('tarefa',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('texto', sa.String(length=1000), nullable=True),
    sa.Column('data', sa.DateTime(timezone=True), nullable=True),
    sa.Column('usuario_id', sa.Integer(), nullable=True),
    sa.Column('publica', sa.Boolean(), nullable=True),
    sa.Column('status_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['status_id'], ['estado.id'], ),
    sa.ForeignKeyConstraint(['usuario_id'], ['usuario.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tarefa')
    op.drop_table('usuario')
    op.drop_table('estado')
    # ### end Alembic commands ###
