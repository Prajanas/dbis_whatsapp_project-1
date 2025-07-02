import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='opq682003',
    database='whatsapp'
)

# csv files and their corresponding table names
csv_files = {
    'media': './data/media.csv',
    'user_table': './data/user_table.csv',
    'user_settings': './data/user_settings.csv',
    'group_member': './data/group_member.csv',
    'personal_message': './data/personal_message.csv',
    'user_contacts': './data/user_contacts.csv',
    'group_table': './data/group_table.csv',
    'status_update': './data/status_update.csv',
    'group_message': './data/group_message.csv'
}

# read csv files
media = pd.read_csv(csv_files['media'])
user_table = pd.read_csv(csv_files['user_table'])
user_settings = pd.read_csv(csv_files['user_settings'])
group_member = pd.read_csv(csv_files['group_member'])
personal_message = pd.read_csv(csv_files['personal_message'])
user_contacts = pd.read_csv(csv_files['user_contacts'])
group_table = pd.read_csv(csv_files['group_table'])
status_update = pd.read_csv(csv_files['status_update'])
group_message = pd.read_csv(csv_files['group_message'])

# create cursor
cursor = conn.cursor()

# insert data into tables
# media
for index, row in media.iterrows():
    row = row.where(pd.notnull(row), None)  # Replace NaN values with None
    cursor.execute("INSERT INTO media (media_id, media_type, media_url) VALUES (%s, %s, %s)",
                   (row['media_id'], row['media_type'], row['media_url']))

# user_table
for index, row in user_table.iterrows():
    row = row.where(pd.notnull(row), None)  # Replace NaN values with None
    cursor.execute("INSERT INTO user_table (user_id, user_name, phone_number, profile_picture, user_status, user_about, last_seen) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (row['user_id'], row['user_name'], row['phone_number'], row['profile_picture'], row['user_status'], row['user_about'], row['last_seen']))


# user_settings
for index, row in user_settings.iterrows():
    row = row.where(pd.notnull(row), None)  # Replace NaN values with None
    cursor.execute("INSERT INTO user_settings (user_id, sound_notification, last_seen_visibility, profile_picture_visibility, read_receipt, dark_mode, app_language) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (row['user_id'], row['sound_notification'], row['last_seen_visibility'], row['profile_picture_visibility'], row['read_receipt'], row['dark_mode'], row['app_language']))

# group_member
for index, row in group_member.iterrows():
    row = row.where(pd.notnull(row), None)  # Replace NaN values with None
    cursor.execute("INSERT INTO group_member (user_id, group_id, user_role, joined_date) VALUES (%s, %s, %s, %s)",
                   (row['user_id'], row['group_id'], row['user_role'], row['joined_date']))

# personal_message
for index, row in personal_message.iterrows():
    row = row.where(pd.notnull(row), None)  # Replace NaN values with None
    cursor.execute("INSERT INTO personal_message (message_id, sender_id, receiver_id, last_update, created_at, message_text, message_media, seen, delivered) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (row['message_id'], row['sender_id'], row['receiver_id'], row['last_update'], row['created_at'], row['message_text'], row['message_media'], row['seen'], row['delivered']))

# user_contacts
for index, row in user_contacts.iterrows():
    row = row.where(pd.notnull(row), None)  # Replace NaN values with None
    cursor.execute("INSERT INTO user_contacts (user_id, person_id, person_name, isBlocked) VALUES (%s, %s, %s, %s)",
                   (row['user_id'], row['person_id'], row['person_name'], row['isBlocked']))

# group_table
for index, row in group_table.iterrows():
    row = row.where(pd.notnull(row), None)  # Replace NaN values with None
    cursor.execute("INSERT INTO group_table (group_id, group_name, group_picture, creation_date, group_description) VALUES (%s, %s, %s, %s, %s)",
                   (row['group_id'], row['group_name'], row['group_picture'], row['creation_date'], row['group_description']))

# status_update
for index, row in status_update.iterrows():
    row = row.where(pd.notnull(row), None)  # Replace NaN values with None
    cursor.execute("INSERT INTO status_update (status_id, user_id, status_media, status_text, last_update) VALUES (%s, %s, %s, %s, %s)",
                   (row['status_id'], row['user_id'], row['status_media'], row['status_text'], row['last_update']))

# group_message
for index, row in group_message.iterrows():
    row = row.where(pd.notnull(row), None)  # Replace NaN values with None
    cursor.execute("INSERT INTO group_message (message_id, sender_id, group_id, last_update, created_at, message_text, message_media) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (row['message_id'], row['sender_id'], row['group_id'], row['last_update'], row['created_at'], row['message_text'], row['message_media']))

# commit changes
conn.commit()

# close connection
conn.close()

