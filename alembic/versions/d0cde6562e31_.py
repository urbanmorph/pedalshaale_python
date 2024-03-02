"""empty message

Revision ID: d0cde6562e31
Revises: 6ad489baad27
Create Date: 2024-03-01 12:15:37.177313

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'd0cde6562e31'
down_revision: Union[str, None] = '6ad489baad27'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    #op.drop_table('sessions')
    #op.drop_table('participants')
    #op.drop_table('admin')
    #op.drop_table('organisation')
    #op.drop_table('training_locations_list')
    #op.drop_table('feedback')
    #op.drop_table('trainer')
    #op.drop_table('users_signup')
    # ### end Alembic commands ###
    pass

def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_signup',
    sa.Column('user_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('contact_no', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('role', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_time', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('user_id', name='users_signup_pkey'),
    sa.UniqueConstraint('contact_no', name='users_signup_contact_no_key')
    )
    op.create_table('trainer',
    sa.Column('trainer_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('trainer_name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('trainer_email', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('trainer_contact', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('trainer_address', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('trainer_age', postgresql.INTERVAL(fields='year'), autoincrement=False, nullable=True),
    sa.Column('trainer_gender', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('trainer_education', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('trainer_aadhar_no', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('trainer_created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('trainer_updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('trainer_training_completion_date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('training_location_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('organisation_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('trainer_language', postgresql.ARRAY(sa.TEXT()), autoincrement=False, nullable=True),
    sa.Column('trainer_status', sa.VARCHAR(length=50), server_default=sa.text("'NOT CERTIFIED'::character varying"), autoincrement=False, nullable=False),
    sa.Column('trainer_code', sa.VARCHAR(length=20), server_default=sa.text("'PST2023X'::character varying"), autoincrement=False, nullable=False),
    sa.CheckConstraint("trainer_status::text = ANY (ARRAY['NOT CERTIFIED'::character varying, 'ONGOING CERTIFICATION'::character varying, 'CERTIFIED'::character varying]::text[])", name='trainer_trainer_status_check'),
    sa.PrimaryKeyConstraint('trainer_id', name='trainer_pkey')
    )
    op.create_table('feedback',
    sa.Column('feedback_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('participant_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('rate_training_sessions', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('learner_guide_useful', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('feedback', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('confident_to_ride', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('trainer_evaluation', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('trainer_feedback', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('feedback_status', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('feedback_id', name='feedback_pkey')
    )
    op.create_table('training_locations_list',
    sa.Column('training_location_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('training_location', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('training_location_address', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('training_location_latitude', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('training_location_longitude', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('training_location_created', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('training_location_updated', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('training_location_picture', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('training_location_id', name='training_locations_list_pkey')
    )
    op.create_table('organisation',
    sa.Column('organisation_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('organisation_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('organisation_address', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('organisation_contact', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('organisation_email', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('organisation_type', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('organisation_activities', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('organisation_legal_status_document', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('coordinator_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('coordinator_email', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('organisation_created_at', postgresql.TIMESTAMP(), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('organisation_updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('coordinator_contact', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('organisation_id', name='organisation_pkey')
    )
    op.create_table('admin',
    sa.Column('contact_no', sa.VARCHAR(length=20), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=100), autoincrement=False, nullable=False)
    )
    op.create_table('participants',
    sa.Column('participant_id', sa.INTEGER(), server_default=sa.text("nextval('participants_participant_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('participant_name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('participant_email', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('participant_contact', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('participant_address', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('participant_age', sa.VARCHAR(length=10), autoincrement=False, nullable=True),
    sa.Column('participant_gender', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('training_location_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('participant_created_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('participant_updated_at', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('participant_status', sa.VARCHAR(length=20), server_default=sa.text("'new'::character varying"), autoincrement=False, nullable=True),
    sa.Column('participant_code', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('feedback_status', sa.VARCHAR(length=20), autoincrement=False, nullable=True),
    sa.Column('training_start_date', postgresql.TIMESTAMP(), server_default=sa.text("'0001-01-01 00:00:00'::timestamp without time zone"), autoincrement=False, nullable=True),
    sa.Column('training_end_date', postgresql.TIMESTAMP(), server_default=sa.text("'0001-01-01 00:00:00'::timestamp without time zone"), autoincrement=False, nullable=True),
    sa.CheckConstraint("participant_status::text = ANY (ARRAY['NEW'::character varying::text, 'ONGOING'::character varying::text, 'COMPLETED'::character varying::text, 'CERTIFIED'::character varying::text, 'DROP-OUT'::character varying::text])", name='new_participants_participant_status_check'),
    sa.PrimaryKeyConstraint('participant_id', name='participants_pkey')
    )
    op.create_table('sessions',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('trainer_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('participant_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('scheduled_datetime', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('actual_datetime', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('hours_trained', sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('picture_path', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('video_path', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('description', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('session_current_date', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('session_update_date', postgresql.TIMESTAMP(), server_default=sa.text('CURRENT_TIMESTAMP'), autoincrement=False, nullable=True),
    sa.Column('session_status', sa.VARCHAR(), server_default=sa.text("'NEW'::character varying"), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='sessions_pkey')
    )
    # ### end Alembic commands ###
