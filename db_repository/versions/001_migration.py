from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
Test = Table('Test', pre_meta,
    Column('parent_id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('root', VARCHAR(length=64)),
)

Us = Table('Us', pre_meta,
    Column('parent_id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('root', VARCHAR(length=64)),
)

auction_auction = Table('auction_auction', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('thumbnail', VARCHAR(length=100)),
    Column('travel_date', DATE),
    Column('time_from', TIME),
    Column('time_to', TIME),
    Column('active_from', DATETIME),
    Column('active_to', DATETIME),
    Column('hide_source', TINYINT(display_width=1), nullable=False),
    Column('hide_destination', TINYINT(display_width=1), nullable=False),
    Column('hide_travel_date', TINYINT(display_width=1), nullable=False),
    Column('minimum_bid', INTEGER(display_width=11)),
    Column('minimum_increment', INTEGER(display_width=11), nullable=False),
    Column('increment_type', VARCHAR(length=20)),
    Column('celebrity_id', INTEGER(display_width=11), nullable=False),
    Column('location_from_id', INTEGER(display_width=11)),
    Column('location_to_id', INTEGER(display_width=11)),
    Column('hide_travel_time', TINYINT(display_width=1), nullable=False),
    Column('status', VARCHAR(length=20)),
    Column('message1', LONGTEXT, nullable=False),
    Column('message2', LONGTEXT, nullable=False),
    Column('final_round_time_in_minutes', INTEGER(display_width=11), nullable=False),
    Column('winner_id', INTEGER(display_width=11)),
)

auction_auction_charities = Table('auction_auction_charities', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('auction_id', INTEGER(display_width=11), nullable=False),
    Column('charity_id', INTEGER(display_width=11), nullable=False),
)

auction_auctionbid = Table('auction_auctionbid', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('current_bid', INTEGER(display_width=11)),
    Column('maximum_bid', INTEGER(display_width=11)),
    Column('status', VARCHAR(length=20)),
    Column('auction_id', INTEGER(display_width=11), nullable=False),
    Column('user_id', INTEGER(display_width=11), nullable=False),
    Column('has_payed', TINYINT(display_width=1), nullable=False),
)

auction_dreambig = Table('auction_dreambig', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('celebrity', VARCHAR(length=200), nullable=False),
    Column('maximum_bid', INTEGER(display_width=11)),
    Column('user_id', INTEGER(display_width=11), nullable=False),
)

auth_group = Table('auth_group', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('name', VARCHAR(length=80), nullable=False),
)

auth_group_permissions = Table('auth_group_permissions', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('group_id', INTEGER(display_width=11), nullable=False),
    Column('permission_id', INTEGER(display_width=11), nullable=False),
)

auth_permission = Table('auth_permission', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('name', VARCHAR(length=50), nullable=False),
    Column('content_type_id', INTEGER(display_width=11), nullable=False),
    Column('codename', VARCHAR(length=100), nullable=False),
)

auth_user = Table('auth_user', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('password', VARCHAR(length=128), nullable=False),
    Column('last_login', DATETIME, nullable=False),
    Column('is_superuser', TINYINT(display_width=1), nullable=False),
    Column('username', VARCHAR(length=30), nullable=False),
    Column('first_name', VARCHAR(length=30), nullable=False),
    Column('last_name', VARCHAR(length=30), nullable=False),
    Column('email', VARCHAR(length=75), nullable=False),
    Column('is_staff', TINYINT(display_width=1), nullable=False),
    Column('is_active', TINYINT(display_width=1), nullable=False),
    Column('date_joined', DATETIME, nullable=False),
)

auth_user_groups = Table('auth_user_groups', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('user_id', INTEGER(display_width=11), nullable=False),
    Column('group_id', INTEGER(display_width=11), nullable=False),
)

auth_user_user_permissions = Table('auth_user_user_permissions', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('user_id', INTEGER(display_width=11), nullable=False),
    Column('permission_id', INTEGER(display_width=11), nullable=False),
)

base_category = Table('base_category', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('name', VARCHAR(length=200), nullable=False),
)

base_city = Table('base_city', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('name', VARCHAR(length=200), nullable=False),
    Column('has_airport', TINYINT(display_width=1), nullable=False),
    Column('country_id', INTEGER(display_width=11), nullable=False),
)

base_country = Table('base_country', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('name', VARCHAR(length=200), nullable=False),
)

base_documenttype = Table('base_documenttype', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('name', VARCHAR(length=200), nullable=False),
)

base_systemsetting = Table('base_systemsetting', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('service_tax', VARCHAR(length=20)),
    Column('bid_leverage', INTEGER(display_width=11)),
)

celebrity_celebrity = Table('celebrity_celebrity', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('first_name', VARCHAR(length=200), nullable=False),
    Column('last_name', VARCHAR(length=200), nullable=False),
    Column('picture', VARCHAR(length=100)),
    Column('category_id', INTEGER(display_width=11), nullable=False),
    Column('gender', VARCHAR(length=10)),
    Column('celebrity_url', VARCHAR(length=200)),
    Column('featured', TINYINT(display_width=1), nullable=False),
    Column('description', LONGTEXT, nullable=False),
    Column('rating_id', INTEGER(display_width=11)),
    Column('status', CHAR(length=1)),
)

celebrity_celebrity_charities = Table('celebrity_celebrity_charities', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('celebrity_id', INTEGER(display_width=11), nullable=False),
    Column('charity_id', INTEGER(display_width=11), nullable=False),
)

celebrity_celebrityrating = Table('celebrity_celebrityrating', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('rating_order', INTEGER(display_width=11), nullable=False),
    Column('rating_value', VARCHAR(length=10), nullable=False),
)

celebrity_charity = Table('celebrity_charity', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('name', VARCHAR(length=200), nullable=False),
    Column('date_of_establishment', DATETIME),
    Column('first_name', VARCHAR(length=200), nullable=False),
    Column('last_name', VARCHAR(length=200), nullable=False),
    Column('email', VARCHAR(length=75)),
    Column('mobile_number', VARCHAR(length=20)),
    Column('gender', VARCHAR(length=10)),
    Column('status', TINYINT(display_width=1), nullable=False),
    Column('picture', VARCHAR(length=100)),
    Column('description', LONGTEXT),
)

columns_priv = Table('columns_priv', pre_meta,
    Column('Host', CHAR(collation='utf8_bin', length=60), primary_key=True, nullable=False),
    Column('Db', CHAR(collation='utf8_bin', length=64), primary_key=True, nullable=False),
    Column('User', CHAR(collation='utf8_bin', length=16), primary_key=True, nullable=False),
    Column('Table_name', CHAR(collation='utf8_bin', length=64), primary_key=True, nullable=False),
    Column('Column_name', CHAR(collation='utf8_bin', length=64), primary_key=True, nullable=False),
    Column('Timestamp', TIMESTAMP, nullable=False),
    Column('Column_priv', SET(charset='utf8', length=10), nullable=False),
)

contest_contest = Table('contest_contest', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('description', LONGTEXT, nullable=False),
    Column('thumbnail', VARCHAR(length=100)),
    Column('donation_type', VARCHAR(length=20)),
    Column('donation_value', INTEGER(display_width=11)),
    Column('reserve_price', INTEGER(display_width=11)),
    Column('start_date', DATETIME),
    Column('end_date', DATETIME),
    Column('draw_date', DATETIME),
    Column('celebrity_id', INTEGER(display_width=11), nullable=False),
    Column('status', VARCHAR(length=20)),
    Column('hide_destination', TINYINT(display_width=1), nullable=False),
    Column('hide_source', TINYINT(display_width=1), nullable=False),
    Column('hide_travel_date', TINYINT(display_width=1), nullable=False),
    Column('hide_travel_time', TINYINT(display_width=1), nullable=False),
    Column('location_from_id', INTEGER(display_width=11)),
    Column('location_to_id', INTEGER(display_width=11)),
    Column('time_from', TIME),
    Column('time_to', TIME),
    Column('travel_date', DATE),
)

contest_contest_charities = Table('contest_contest_charities', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('contest_id', INTEGER(display_width=11), nullable=False),
    Column('charity_id', INTEGER(display_width=11), nullable=False),
)

contest_contestparticipant = Table('contest_contestparticipant', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('number_of_chances', INTEGER(display_width=11), nullable=False),
    Column('quiz_taken', TINYINT(display_width=1), nullable=False),
    Column('is_winner', TINYINT(display_width=1), nullable=False),
    Column('contest_id', INTEGER(display_width=11), nullable=False),
    Column('user_id', INTEGER(display_width=11), nullable=False),
    Column('is_selected', TINYINT(display_width=1), nullable=False),
)

contest_contestpayment = Table('contest_contestpayment', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('payment_method', VARCHAR(length=20)),
    Column('payment_value', INTEGER(display_width=11), nullable=False),
    Column('object_id', INTEGER(display_width=10, unsigned=True), nullable=False),
    Column('content_type_id', INTEGER(display_width=11), nullable=False),
    Column('contest_id', INTEGER(display_width=11), nullable=False),
    Column('contest_participant_id', INTEGER(display_width=11), nullable=False),
    Column('user_id', INTEGER(display_width=11), nullable=False),
)

contest_contestquestion = Table('contest_contestquestion', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('question', LONGTEXT, nullable=False),
    Column('status', TINYINT(display_width=1), nullable=False),
    Column('contest_id', INTEGER(display_width=11), nullable=False),
)

contest_questionoption = Table('contest_questionoption', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('option', LONGTEXT, nullable=False),
    Column('is_correct', TINYINT(display_width=1), nullable=False),
    Column('status', TINYINT(display_width=1), nullable=False),
    Column('question_id', INTEGER(display_width=11), nullable=False),
)

contest_scratchcard = Table('contest_scratchcard', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('scratch_code', VARCHAR(length=20), nullable=False),
    Column('used', TINYINT(display_width=1), nullable=False),
    Column('value', INTEGER(display_width=11), nullable=False),
    Column('contest_id', INTEGER(display_width=11)),
    Column('used_by_id', INTEGER(display_width=11)),
)

db = Table('db', pre_meta,
    Column('Host', CHAR(collation='utf8_bin', length=60), primary_key=True, nullable=False),
    Column('Db', CHAR(collation='utf8_bin', length=64), primary_key=True, nullable=False),
    Column('User', CHAR(collation='utf8_bin', length=16), primary_key=True, nullable=False),
    Column('Select_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Insert_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Update_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Delete_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Create_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Drop_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Grant_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('References_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Index_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Alter_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Create_tmp_table_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Lock_tables_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Create_view_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Show_view_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Create_routine_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Alter_routine_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Execute_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Event_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Trigger_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
)

django_admin_log = Table('django_admin_log', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('action_time', DATETIME, nullable=False),
    Column('object_id', LONGTEXT),
    Column('object_repr', VARCHAR(length=200), nullable=False),
    Column('action_flag', SMALLINT(display_width=5, unsigned=True), nullable=False),
    Column('change_message', LONGTEXT, nullable=False),
    Column('content_type_id', INTEGER(display_width=11)),
    Column('user_id', INTEGER(display_width=11), nullable=False),
)

django_content_type = Table('django_content_type', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('name', VARCHAR(length=100), nullable=False),
    Column('app_label', VARCHAR(length=100), nullable=False),
    Column('model', VARCHAR(length=100), nullable=False),
)

django_migrations = Table('django_migrations', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('app', VARCHAR(length=255), nullable=False),
    Column('name', VARCHAR(length=255), nullable=False),
    Column('applied', DATETIME, nullable=False),
)

django_session = Table('django_session', pre_meta,
    Column('session_key', VARCHAR(length=40), primary_key=True, nullable=False),
    Column('session_data', LONGTEXT, nullable=False),
    Column('expire_date', DATETIME, nullable=False),
)

event = Table('event', pre_meta,
    Column('db', CHAR(charset='utf8', collation='utf8_bin', length=64), primary_key=True, nullable=False),
    Column('name', CHAR(length=64), primary_key=True, nullable=False),
    Column('body', LONGBLOB, nullable=False),
    Column('definer', CHAR(charset='utf8', collation='utf8_bin', length=77), nullable=False),
    Column('execute_at', DATETIME),
    Column('interval_value', INTEGER(display_width=11)),
    Column('interval_field', ENUM('YEAR', 'QUARTER', 'MONTH', 'DAY', 'HOUR', 'MINUTE', 'WEEK', 'SECOND', 'MICROSECOND', 'YEAR_MONTH', 'DAY_HOUR', 'DAY_MINUTE', 'DAY_SECOND', 'HOUR_MINUTE', 'HOUR_SECOND', 'MINUTE_SECOND', 'DAY_MICROSECOND', 'HOUR_MICROSECOND', 'MINUTE_MICROSECOND', 'SECOND_MICROSECOND')),
    Column('created', TIMESTAMP, nullable=False),
    Column('modified', TIMESTAMP, nullable=False),
    Column('last_executed', DATETIME),
    Column('starts', DATETIME),
    Column('ends', DATETIME),
    Column('status', ENUM('ENABLED', 'DISABLED', 'SLAVESIDE_DISABLED'), nullable=False),
    Column('on_completion', ENUM('DROP', 'PRESERVE'), nullable=False),
    Column('sql_mode', SET(length=26), nullable=False),
    Column('comment', CHAR(charset='utf8', collation='utf8_bin', length=64), nullable=False),
    Column('originator', INTEGER(display_width=10, unsigned=True), nullable=False),
    Column('time_zone', CHAR(charset='latin1', length=64), nullable=False),
    Column('character_set_client', CHAR(charset='utf8', collation='utf8_bin', length=32)),
    Column('collation_connection', CHAR(charset='utf8', collation='utf8_bin', length=32)),
    Column('db_collation', CHAR(charset='utf8', collation='utf8_bin', length=32)),
    Column('body_utf8', LONGBLOB),
)

func = Table('func', pre_meta,
    Column('name', CHAR(collation='utf8_bin', length=64), primary_key=True, nullable=False),
    Column('ret', TINYINT(display_width=1), nullable=False),
    Column('dl', CHAR(collation='utf8_bin', length=128), nullable=False),
    Column('type', ENUM('function', 'aggregate', charset='utf8'), nullable=False),
)

general_log = Table('general_log', pre_meta,
    Column('event_time', TIMESTAMP, nullable=False),
    Column('user_host', MEDIUMTEXT, nullable=False),
    Column('thread_id', INTEGER(display_width=11), nullable=False),
    Column('server_id', INTEGER(display_width=10, unsigned=True), nullable=False),
    Column('command_type', VARCHAR(length=64), nullable=False),
    Column('argument', MEDIUMTEXT, nullable=False),
)

help_category = Table('help_category', pre_meta,
    Column('help_category_id', SMALLINT(display_width=5, unsigned=True), primary_key=True, nullable=False),
    Column('name', CHAR(length=64), nullable=False),
    Column('parent_category_id', SMALLINT(display_width=5, unsigned=True)),
    Column('url', TEXT, nullable=False),
)

help_keyword = Table('help_keyword', pre_meta,
    Column('help_keyword_id', INTEGER(display_width=10, unsigned=True), primary_key=True, nullable=False),
    Column('name', CHAR(length=64), nullable=False),
)

help_relation = Table('help_relation', pre_meta,
    Column('help_topic_id', INTEGER(display_width=10, unsigned=True), primary_key=True, nullable=False),
    Column('help_keyword_id', INTEGER(display_width=10, unsigned=True), primary_key=True, nullable=False),
)

help_topic = Table('help_topic', pre_meta,
    Column('help_topic_id', INTEGER(display_width=10, unsigned=True), primary_key=True, nullable=False),
    Column('name', CHAR(length=64), nullable=False),
    Column('help_category_id', SMALLINT(display_width=5, unsigned=True), nullable=False),
    Column('description', TEXT, nullable=False),
    Column('example', TEXT, nullable=False),
    Column('url', TEXT, nullable=False),
)

host = Table('host', pre_meta,
    Column('Host', CHAR(collation='utf8_bin', length=60), primary_key=True, nullable=False),
    Column('Db', CHAR(collation='utf8_bin', length=64), primary_key=True, nullable=False),
    Column('Select_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Insert_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Update_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Delete_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Create_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Drop_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Grant_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('References_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Index_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Alter_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Create_tmp_table_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Lock_tables_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Create_view_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Show_view_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Create_routine_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Alter_routine_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Execute_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Trigger_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
)

ndb_binlog_index = Table('ndb_binlog_index', pre_meta,
    Column('Position', BIGINT(display_width=20, unsigned=True), nullable=False),
    Column('File', VARCHAR(length=255), nullable=False),
    Column('epoch', BIGINT(display_width=20, unsigned=True), primary_key=True, nullable=False),
    Column('inserts', BIGINT(display_width=20, unsigned=True), nullable=False),
    Column('updates', BIGINT(display_width=20, unsigned=True), nullable=False),
    Column('deletes', BIGINT(display_width=20, unsigned=True), nullable=False),
    Column('schemaops', BIGINT(display_width=20, unsigned=True), nullable=False),
)

plugin = Table('plugin', pre_meta,
    Column('name', VARCHAR(length=64), primary_key=True, nullable=False),
    Column('dl', VARCHAR(length=128), nullable=False),
)

proc = Table('proc', pre_meta,
    Column('db', CHAR(charset='utf8', collation='utf8_bin', length=64), primary_key=True, nullable=False),
    Column('name', CHAR(length=64), primary_key=True, nullable=False),
    Column('type', ENUM('FUNCTION', 'PROCEDURE'), primary_key=True, nullable=False),
    Column('specific_name', CHAR(length=64), nullable=False),
    Column('language', ENUM('SQL'), nullable=False),
    Column('sql_data_access', ENUM('CONTAINS_SQL', 'NO_SQL', 'READS_SQL_DATA', 'MODIFIES_SQL_DATA'), nullable=False),
    Column('is_deterministic', ENUM('YES', 'NO'), nullable=False),
    Column('security_type', ENUM('INVOKER', 'DEFINER'), nullable=False),
    Column('param_list', BLOB, nullable=False),
    Column('returns', LONGBLOB, nullable=False),
    Column('body', LONGBLOB, nullable=False),
    Column('definer', CHAR(charset='utf8', collation='utf8_bin', length=77), nullable=False),
    Column('created', TIMESTAMP, nullable=False),
    Column('modified', TIMESTAMP, nullable=False),
    Column('sql_mode', SET(length=26), nullable=False),
    Column('comment', TEXT(charset='utf8', collation='utf8_bin'), nullable=False),
    Column('character_set_client', CHAR(charset='utf8', collation='utf8_bin', length=32)),
    Column('collation_connection', CHAR(charset='utf8', collation='utf8_bin', length=32)),
    Column('db_collation', CHAR(charset='utf8', collation='utf8_bin', length=32)),
    Column('body_utf8', LONGBLOB),
)

procs_priv = Table('procs_priv', pre_meta,
    Column('Host', CHAR(collation='utf8_bin', length=60), primary_key=True, nullable=False),
    Column('Db', CHAR(collation='utf8_bin', length=64), primary_key=True, nullable=False),
    Column('User', CHAR(collation='utf8_bin', length=16), primary_key=True, nullable=False),
    Column('Routine_name', CHAR(charset='utf8', length=64), primary_key=True, nullable=False),
    Column('Routine_type', ENUM('FUNCTION', 'PROCEDURE', collation='utf8_bin'), primary_key=True, nullable=False),
    Column('Grantor', CHAR(collation='utf8_bin', length=77), nullable=False),
    Column('Proc_priv', SET(charset='utf8', length=13), nullable=False),
    Column('Timestamp', TIMESTAMP, nullable=False),
)

proxies_priv = Table('proxies_priv', pre_meta,
    Column('Host', CHAR(collation='utf8_bin', length=60), primary_key=True, nullable=False),
    Column('User', CHAR(collation='utf8_bin', length=16), primary_key=True, nullable=False),
    Column('Proxied_host', CHAR(collation='utf8_bin', length=60), primary_key=True, nullable=False),
    Column('Proxied_user', CHAR(collation='utf8_bin', length=16), primary_key=True, nullable=False),
    Column('With_grant', TINYINT(display_width=1), nullable=False),
    Column('Grantor', CHAR(collation='utf8_bin', length=77), nullable=False),
    Column('Timestamp', TIMESTAMP, nullable=False),
)

servers = Table('servers', pre_meta,
    Column('Server_name', CHAR(length=64), primary_key=True, nullable=False),
    Column('Host', CHAR(length=64), nullable=False),
    Column('Db', CHAR(length=64), nullable=False),
    Column('Username', CHAR(length=64), nullable=False),
    Column('Password', CHAR(length=64), nullable=False),
    Column('Port', INTEGER(display_width=4), nullable=False),
    Column('Socket', CHAR(length=64), nullable=False),
    Column('Wrapper', CHAR(length=64), nullable=False),
    Column('Owner', CHAR(length=64), nullable=False),
)

slow_log = Table('slow_log', pre_meta,
    Column('start_time', TIMESTAMP, nullable=False),
    Column('user_host', MEDIUMTEXT, nullable=False),
    Column('query_time', TIME, nullable=False),
    Column('lock_time', TIME, nullable=False),
    Column('rows_sent', INTEGER(display_width=11), nullable=False),
    Column('rows_examined', INTEGER(display_width=11), nullable=False),
    Column('db', VARCHAR(length=512), nullable=False),
    Column('last_insert_id', INTEGER(display_width=11), nullable=False),
    Column('insert_id', INTEGER(display_width=11), nullable=False),
    Column('server_id', INTEGER(display_width=10, unsigned=True), nullable=False),
    Column('sql_text', MEDIUMTEXT, nullable=False),
)

social_auth_association = Table('social_auth_association', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('server_url', VARCHAR(length=255), nullable=False),
    Column('handle', VARCHAR(length=255), nullable=False),
    Column('secret', VARCHAR(length=255), nullable=False),
    Column('issued', INTEGER(display_width=11), nullable=False),
    Column('lifetime', INTEGER(display_width=11), nullable=False),
    Column('assoc_type', VARCHAR(length=64), nullable=False),
)

social_auth_code = Table('social_auth_code', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('email', VARCHAR(length=75), nullable=False),
    Column('code', VARCHAR(length=32), nullable=False),
    Column('verified', TINYINT(display_width=1), nullable=False),
)

social_auth_nonce = Table('social_auth_nonce', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('server_url', VARCHAR(length=255), nullable=False),
    Column('timestamp', INTEGER(display_width=11), nullable=False),
    Column('salt', VARCHAR(length=65), nullable=False),
)

social_auth_usersocialauth = Table('social_auth_usersocialauth', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('provider', VARCHAR(length=32), nullable=False),
    Column('uid', VARCHAR(length=255), nullable=False),
    Column('extra_data', LONGTEXT, nullable=False),
    Column('user_id', INTEGER(display_width=11), nullable=False),
)

table1 = Table('table1', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('nickname', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
)

tables_priv = Table('tables_priv', pre_meta,
    Column('Host', CHAR(collation='utf8_bin', length=60), primary_key=True, nullable=False),
    Column('Db', CHAR(collation='utf8_bin', length=64), primary_key=True, nullable=False),
    Column('User', CHAR(collation='utf8_bin', length=16), primary_key=True, nullable=False),
    Column('Table_name', CHAR(collation='utf8_bin', length=64), primary_key=True, nullable=False),
    Column('Grantor', CHAR(collation='utf8_bin', length=77), nullable=False),
    Column('Timestamp', TIMESTAMP, nullable=False),
    Column('Table_priv', SET(charset='utf8', length=11), nullable=False),
    Column('Column_priv', SET(charset='utf8', length=10), nullable=False),
)

time_zone = Table('time_zone', pre_meta,
    Column('Time_zone_id', INTEGER(display_width=10, unsigned=True), primary_key=True, nullable=False),
    Column('Use_leap_seconds', ENUM('Y', 'N'), nullable=False),
)

time_zone_leap_second = Table('time_zone_leap_second', pre_meta,
    Column('Transition_time', BIGINT(display_width=20), primary_key=True, nullable=False),
    Column('Correction', INTEGER(display_width=11), nullable=False),
)

time_zone_name = Table('time_zone_name', pre_meta,
    Column('Name', CHAR(length=64), primary_key=True, nullable=False),
    Column('Time_zone_id', INTEGER(display_width=10, unsigned=True), nullable=False),
)

time_zone_transition = Table('time_zone_transition', pre_meta,
    Column('Time_zone_id', INTEGER(display_width=10, unsigned=True), primary_key=True, nullable=False),
    Column('Transition_time', BIGINT(display_width=20), primary_key=True, nullable=False),
    Column('Transition_type_id', INTEGER(display_width=10, unsigned=True), nullable=False),
)

time_zone_transition_type = Table('time_zone_transition_type', pre_meta,
    Column('Time_zone_id', INTEGER(display_width=10, unsigned=True), primary_key=True, nullable=False),
    Column('Transition_type_id', INTEGER(display_width=10, unsigned=True), primary_key=True, nullable=False),
    Column('Offset', INTEGER(display_width=11), nullable=False),
    Column('Is_DST', TINYINT(display_width=3, unsigned=True), nullable=False),
    Column('Abbreviation', CHAR(length=8), nullable=False),
)

us = Table('us', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('root', VARCHAR(length=64)),
)

use = Table('use', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('root', VARCHAR(length=64)),
)

user = Table('user', pre_meta,
    Column('Host', CHAR(collation='utf8_bin', length=60), primary_key=True, nullable=False),
    Column('User', CHAR(collation='utf8_bin', length=16), primary_key=True, nullable=False),
    Column('Password', CHAR(charset='latin1', collation='latin1_bin', length=41), nullable=False),
    Column('Select_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Insert_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Update_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Delete_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Create_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Drop_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Reload_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Shutdown_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Process_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('File_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Grant_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('References_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Index_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Alter_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Show_db_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Super_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Create_tmp_table_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Lock_tables_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Execute_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Repl_slave_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Repl_client_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Create_view_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Show_view_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Create_routine_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Alter_routine_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Create_user_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Event_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Trigger_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('Create_tablespace_priv', ENUM('N', 'Y', charset='utf8'), nullable=False),
    Column('ssl_type', ENUM('', 'ANY', 'X509', 'SPECIFIED', charset='utf8'), nullable=False),
    Column('ssl_cipher', BLOB, nullable=False),
    Column('x509_issuer', BLOB, nullable=False),
    Column('x509_subject', BLOB, nullable=False),
    Column('max_questions', INTEGER(display_width=11, unsigned=True), nullable=False),
    Column('max_updates', INTEGER(display_width=11, unsigned=True), nullable=False),
    Column('max_connections', INTEGER(display_width=11, unsigned=True), nullable=False),
    Column('max_user_connections', INTEGER(display_width=11, unsigned=True), nullable=False),
    Column('plugin', CHAR(collation='utf8_bin', length=64)),
    Column('authentication_string', TEXT(collation='utf8_bin')),
)

useraccount_auctiongift = Table('useraccount_auctiongift', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('auction_bid_id', INTEGER(display_width=11), nullable=False),
    Column('giftee_id', INTEGER(display_width=11), nullable=False),
)

useraccount_discountcoupon = Table('useraccount_discountcoupon', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('coupon', VARCHAR(length=20), nullable=False),
    Column('value', INTEGER(display_width=11)),
    Column('value_type', VARCHAR(length=15), nullable=False),
    Column('usage_times', INTEGER(display_width=11), nullable=False),
)

useraccount_gifteedocument = Table('useraccount_gifteedocument', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('document', VARCHAR(length=100), nullable=False),
    Column('document_type_id', INTEGER(display_width=11), nullable=False),
    Column('giftee_id', INTEGER(display_width=11), nullable=False),
)

useraccount_onetimepassword = Table('useraccount_onetimepassword', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('code', VARCHAR(length=6)),
    Column('scode', VARCHAR(length=16), nullable=False),
    Column('expiry_date', DATETIME),
    Column('user_id', INTEGER(display_width=11)),
)

useraccount_paymenttransaction = Table('useraccount_paymenttransaction', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('amount', INTEGER(display_width=11), nullable=False),
    Column('original_amount', INTEGER(display_width=11), nullable=False),
    Column('bank_transaction_id', VARCHAR(length=256)),
    Column('transaction_status', VARCHAR(length=50)),
    Column('payment_mode', VARCHAR(length=50)),
    Column('transaction_message', LONGTEXT),
    Column('payment_via', VARCHAR(length=50)),
    Column('user_id', INTEGER(display_width=11), nullable=False),
    Column('citrus_transaction_id', VARCHAR(length=50)),
    Column('cheque_number', VARCHAR(length=50)),
    Column('reciept_number', VARCHAR(length=50)),
    Column('other_details', VARCHAR(length=500)),
    Column('paytm_transaction_id', VARCHAR(length=50)),
    Column('balance', VARCHAR(length=200)),
    Column('transaction_type', VARCHAR(length=50)),
    Column('discount_coupon_id', INTEGER(display_width=11)),
)

useraccount_refundrequest = Table('useraccount_refundrequest', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('refund_amount', INTEGER(display_width=11), nullable=False),
    Column('refund_status', VARCHAR(length=20), nullable=False),
    Column('payment_transaction_id', INTEGER(display_width=11), nullable=False),
    Column('refunded_amount', INTEGER(display_width=11)),
    Column('user_id', INTEGER(display_width=11), nullable=False),
    Column('has_processed', TINYINT(display_width=1), nullable=False),
)

useraccount_requestcallback = Table('useraccount_requestcallback', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('mobile_number', VARCHAR(length=15)),
    Column('have_called', TINYINT(display_width=1), nullable=False),
    Column('user_id', INTEGER(display_width=11)),
    Column('remarks', LONGTEXT),
)

useraccount_useraccount = Table('useraccount_useraccount', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('amount', VARCHAR(length=200)),
    Column('is_screened', TINYINT(display_width=1), nullable=False),
    Column('is_otp_verified', TINYINT(display_width=1), nullable=False),
    Column('mobile_number', VARCHAR(length=15)),
    Column('user_id', INTEGER(display_width=11), nullable=False),
    Column('address_line1', LONGTEXT),
    Column('address_line2', LONGTEXT),
    Column('city', LONGTEXT),
    Column('pincode', LONGTEXT),
    Column('state', LONGTEXT),
    Column('citizenship', VARCHAR(length=10)),
    Column('date_of_birth', VARCHAR(length=15)),
    Column('gender', VARCHAR(length=10)),
    Column('fwv_balance', VARCHAR(length=200)),
)

useraccount_userdocument = Table('useraccount_userdocument', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('document', VARCHAR(length=100), nullable=False),
    Column('document_type_id', INTEGER(display_width=11), nullable=False),
    Column('user_id', INTEGER(display_width=11), nullable=False),
)

useraccount_usergiftee = Table('useraccount_usergiftee', pre_meta,
    Column('id', INTEGER(display_width=11), primary_key=True, nullable=False),
    Column('date_created', DATETIME, nullable=False),
    Column('last_modified', DATETIME, nullable=False),
    Column('name', VARCHAR(length=100), nullable=False),
    Column('email', VARCHAR(length=75), nullable=False),
    Column('mobile_number', VARCHAR(length=15)),
    Column('user_id', INTEGER(display_width=11), nullable=False),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['Test'].drop()
    pre_meta.tables['Us'].drop()
    pre_meta.tables['auction_auction'].drop()
    pre_meta.tables['auction_auction_charities'].drop()
    pre_meta.tables['auction_auctionbid'].drop()
    pre_meta.tables['auction_dreambig'].drop()
    pre_meta.tables['auth_group'].drop()
    pre_meta.tables['auth_group_permissions'].drop()
    pre_meta.tables['auth_permission'].drop()
    pre_meta.tables['auth_user'].drop()
    pre_meta.tables['auth_user_groups'].drop()
    pre_meta.tables['auth_user_user_permissions'].drop()
    pre_meta.tables['base_category'].drop()
    pre_meta.tables['base_city'].drop()
    pre_meta.tables['base_country'].drop()
    pre_meta.tables['base_documenttype'].drop()
    pre_meta.tables['base_systemsetting'].drop()
    pre_meta.tables['celebrity_celebrity'].drop()
    pre_meta.tables['celebrity_celebrity_charities'].drop()
    pre_meta.tables['celebrity_celebrityrating'].drop()
    pre_meta.tables['celebrity_charity'].drop()
    pre_meta.tables['columns_priv'].drop()
    pre_meta.tables['contest_contest'].drop()
    pre_meta.tables['contest_contest_charities'].drop()
    pre_meta.tables['contest_contestparticipant'].drop()
    pre_meta.tables['contest_contestpayment'].drop()
    pre_meta.tables['contest_contestquestion'].drop()
    pre_meta.tables['contest_questionoption'].drop()
    pre_meta.tables['contest_scratchcard'].drop()
    pre_meta.tables['db'].drop()
    pre_meta.tables['django_admin_log'].drop()
    pre_meta.tables['django_content_type'].drop()
    pre_meta.tables['django_migrations'].drop()
    pre_meta.tables['django_session'].drop()
    pre_meta.tables['event'].drop()
    pre_meta.tables['func'].drop()
    pre_meta.tables['general_log'].drop()
    pre_meta.tables['help_category'].drop()
    pre_meta.tables['help_keyword'].drop()
    pre_meta.tables['help_relation'].drop()
    pre_meta.tables['help_topic'].drop()
    pre_meta.tables['host'].drop()
    pre_meta.tables['ndb_binlog_index'].drop()
    pre_meta.tables['plugin'].drop()
    pre_meta.tables['proc'].drop()
    pre_meta.tables['procs_priv'].drop()
    pre_meta.tables['proxies_priv'].drop()
    pre_meta.tables['servers'].drop()
    pre_meta.tables['slow_log'].drop()
    pre_meta.tables['social_auth_association'].drop()
    pre_meta.tables['social_auth_code'].drop()
    pre_meta.tables['social_auth_nonce'].drop()
    pre_meta.tables['social_auth_usersocialauth'].drop()
    pre_meta.tables['table1'].drop()
    pre_meta.tables['tables_priv'].drop()
    pre_meta.tables['time_zone'].drop()
    pre_meta.tables['time_zone_leap_second'].drop()
    pre_meta.tables['time_zone_name'].drop()
    pre_meta.tables['time_zone_transition'].drop()
    pre_meta.tables['time_zone_transition_type'].drop()
    pre_meta.tables['us'].drop()
    pre_meta.tables['use'].drop()
    pre_meta.tables['user'].drop()
    pre_meta.tables['useraccount_auctiongift'].drop()
    pre_meta.tables['useraccount_discountcoupon'].drop()
    pre_meta.tables['useraccount_gifteedocument'].drop()
    pre_meta.tables['useraccount_onetimepassword'].drop()
    pre_meta.tables['useraccount_paymenttransaction'].drop()
    pre_meta.tables['useraccount_refundrequest'].drop()
    pre_meta.tables['useraccount_requestcallback'].drop()
    pre_meta.tables['useraccount_useraccount'].drop()
    pre_meta.tables['useraccount_userdocument'].drop()
    pre_meta.tables['useraccount_usergiftee'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['Test'].create()
    pre_meta.tables['Us'].create()
    pre_meta.tables['auction_auction'].create()
    pre_meta.tables['auction_auction_charities'].create()
    pre_meta.tables['auction_auctionbid'].create()
    pre_meta.tables['auction_dreambig'].create()
    pre_meta.tables['auth_group'].create()
    pre_meta.tables['auth_group_permissions'].create()
    pre_meta.tables['auth_permission'].create()
    pre_meta.tables['auth_user'].create()
    pre_meta.tables['auth_user_groups'].create()
    pre_meta.tables['auth_user_user_permissions'].create()
    pre_meta.tables['base_category'].create()
    pre_meta.tables['base_city'].create()
    pre_meta.tables['base_country'].create()
    pre_meta.tables['base_documenttype'].create()
    pre_meta.tables['base_systemsetting'].create()
    pre_meta.tables['celebrity_celebrity'].create()
    pre_meta.tables['celebrity_celebrity_charities'].create()
    pre_meta.tables['celebrity_celebrityrating'].create()
    pre_meta.tables['celebrity_charity'].create()
    pre_meta.tables['columns_priv'].create()
    pre_meta.tables['contest_contest'].create()
    pre_meta.tables['contest_contest_charities'].create()
    pre_meta.tables['contest_contestparticipant'].create()
    pre_meta.tables['contest_contestpayment'].create()
    pre_meta.tables['contest_contestquestion'].create()
    pre_meta.tables['contest_questionoption'].create()
    pre_meta.tables['contest_scratchcard'].create()
    pre_meta.tables['db'].create()
    pre_meta.tables['django_admin_log'].create()
    pre_meta.tables['django_content_type'].create()
    pre_meta.tables['django_migrations'].create()
    pre_meta.tables['django_session'].create()
    pre_meta.tables['event'].create()
    pre_meta.tables['func'].create()
    pre_meta.tables['general_log'].create()
    pre_meta.tables['help_category'].create()
    pre_meta.tables['help_keyword'].create()
    pre_meta.tables['help_relation'].create()
    pre_meta.tables['help_topic'].create()
    pre_meta.tables['host'].create()
    pre_meta.tables['ndb_binlog_index'].create()
    pre_meta.tables['plugin'].create()
    pre_meta.tables['proc'].create()
    pre_meta.tables['procs_priv'].create()
    pre_meta.tables['proxies_priv'].create()
    pre_meta.tables['servers'].create()
    pre_meta.tables['slow_log'].create()
    pre_meta.tables['social_auth_association'].create()
    pre_meta.tables['social_auth_code'].create()
    pre_meta.tables['social_auth_nonce'].create()
    pre_meta.tables['social_auth_usersocialauth'].create()
    pre_meta.tables['table1'].create()
    pre_meta.tables['tables_priv'].create()
    pre_meta.tables['time_zone'].create()
    pre_meta.tables['time_zone_leap_second'].create()
    pre_meta.tables['time_zone_name'].create()
    pre_meta.tables['time_zone_transition'].create()
    pre_meta.tables['time_zone_transition_type'].create()
    pre_meta.tables['us'].create()
    pre_meta.tables['use'].create()
    pre_meta.tables['user'].create()
    pre_meta.tables['useraccount_auctiongift'].create()
    pre_meta.tables['useraccount_discountcoupon'].create()
    pre_meta.tables['useraccount_gifteedocument'].create()
    pre_meta.tables['useraccount_onetimepassword'].create()
    pre_meta.tables['useraccount_paymenttransaction'].create()
    pre_meta.tables['useraccount_refundrequest'].create()
    pre_meta.tables['useraccount_requestcallback'].create()
    pre_meta.tables['useraccount_useraccount'].create()
    pre_meta.tables['useraccount_userdocument'].create()
    pre_meta.tables['useraccount_usergiftee'].create()
