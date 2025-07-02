import mysql.connector
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='opq682003',
    database='whatsapp'
)

def get_user_by_id():
    user_id = input("Enter the user ID: ")
    cursor = conn.cursor()
    query = f"SELECT * FROM user_table WHERE user_id = {user_id}"
    cursor.execute(query)
    user_data = cursor.fetchall()
    print(user_data)

def get_user_contact_list_by_id():
    user_id = input("Enter the user ID: ")
    cursor = conn.cursor()
    query = f"SELECT * FROM user_contacts WHERE user_id = {user_id}"
    cursor.execute(query)
    user_contact_list = cursor.fetchall()
    print(user_contact_list)

def get_all_message_for_a_chat_with_media():
    sender_id = input("Enter the sender ID: ")
    receiver_id = input("Enter the receiver ID: ")
    cursor = conn.cursor()
    query = f"SELECT * FROM personal_message JOIN media ON personal_message.message_media = media.media_id WHERE (sender_id = {sender_id} AND receiver_id = {receiver_id}) OR (sender_id = {receiver_id} AND receiver_id = {sender_id})"
    cursor.execute(query)
    message_list = cursor.fetchall()
    print(message_list)

def get_all_message_for_a_group_with_media():
    group_id = input("Enter the group ID: ")
    cursor = conn.cursor()
    query = f"SELECT * FROM group_message JOIN media ON group_message.message_media = media.media_id WHERE group_id = {group_id}"
    cursor.execute(query)
    message_list = cursor.fetchall()
    print(message_list)

def list_all_groups_of_a_user():
    user_id = input("Enter the user ID: ")
    cursor = conn.cursor()
    query = f"SELECT * FROM group_member JOIN group_table ON group_member.group_id = group_table.group_id WHERE user_id = {user_id}"
    cursor.execute(query)
    group_list = cursor.fetchall()
    print(group_list)

def get_information_of_a_group():
    group_id = input("Enter the group ID: ")
    cursor = conn.cursor()
    query = f"SELECT * FROM group_table JOIN media ON group_table.group_picture = media.media_id WHERE group_id = {group_id}"
    cursor.execute(query)
    group_info = cursor.fetchall()
    print(group_info)

def get_last_message_of_all_personal_chat_of_a_user():
    user_id = input("Enter the user ID: ")
    cursor = conn.cursor()
    query = f"SELECT * FROM personal_message WHERE (sender_id = {user_id} OR receiver_id = {user_id})"
    cursor.execute(query)
    message_list = cursor.fetchall()
    print(message_list)

def add_a_new_user_to_a_group():
    user_id = input("Enter the user ID: ")
    group_id = input("Enter the group ID: ")
    user_role = input("Enter the user role: ")
    joined_date = input("Enter the joined date: ")
    cursor = conn.cursor()
    query = f"INSERT INTO group_member (user_id, group_id, user_role, joined_date) VALUES ({user_id}, {group_id}, '{user_role}', '{joined_date}')"
    cursor.execute(query)
    conn.commit()
    print("User added to group")

def send_message_to_a_user():
    message_id = input("Enter the message ID: ")
    sender_id = input("Enter the sender ID: ")
    receiver_id = input("Enter the receiver ID: ")
    last_update = input("Enter the last update: ")
    created_at = input("Enter the created at: ")
    message_text = input("Enter the message text: ")
    media_id = input("Enter the message media: ")
    media_type = input("Enter the media type: ")
    media_url = input("Enter the media url: ")
    cursor = conn.cursor()
    query = f"INSERT INTO media (media_id, media_type, media_url) VALUES ({media_id}, '{media_type}', '{media_url}')"
    cursor.execute(query)
    query = f"INSERT INTO personal_message (message_id, sender_id, receiver_id, last_update, created_at, message_text, message_media) VALUES ({message_id}, {sender_id}, {receiver_id}, '{last_update}', '{created_at}', '{message_text}', {media_id})"
    cursor.execute(query)
    conn.commit()
    print("Message sent")

def send_message_to_a_group():
    message_id = input("Enter the message ID: ")
    sender_id = input("Enter the sender ID: ")
    group_id = input("Enter the group ID: ")
    last_update = input("Enter the last update: ")
    created_at = input("Enter the created at: ")
    message_text = input("Enter the message text: ")
    media_id = input("Enter the message media: ")
    media_type = input("Enter the media type: ")
    media_url = input("Enter the media url: ")
    cursor = conn.cursor()
    query = f"INSERT INTO media (media_id, media_type, media_url) VALUES ({media_id}, '{media_type}', '{media_url}')"
    cursor.execute(query)
    query = f"INSERT INTO group_message (message_id, sender_id, group_id, last_update, created_at, message_text, message_media) VALUES ({message_id}, {sender_id}, {group_id}, '{last_update}', '{created_at}', '{message_text}', {media_id})"
    cursor.execute(query)
    conn.commit()
    print("Message sent")

def begin_a_new_chat():
    user_id = input("Enter the user ID: ")
    person_id = input("Enter the person ID: ")
    person_name = input("Enter the person name: ")
    isBlocked = input("Enter the isBlocked: ")
    cursor = conn.cursor()
    query = f"INSERT INTO user_contacts (user_id, person_id, person_name, isBlocked) VALUES ({user_id}, {person_id}, '{person_name}', {isBlocked})"
    cursor.execute(query)
    conn.commit()
    print("Chat started")

def create_a_new_group():
    group_id = input("Enter the group ID: ")
    group_name = input("Enter the group name: ")
    group_picture = input("Enter the group picture: ")
    creation_date = input("Enter the creation date: ")
    group_description = input("Enter the group description: ")
    cursor = conn.cursor()
    # begin transaction
    query = "BEGIN"
    cursor.execute(query)
    query = f"INSERT INTO media (media_id, media_type, media_url) VALUES ({group_picture}, 'image', 'https://www.google.com')"
    cursor.execute(query)
    query = f"INSERT INTO group_table (group_id, group_name, group_picture, creation_date, group_description) VALUES ({group_id}, '{group_name}', {group_picture}, '{creation_date}', '{group_description}')"
    cursor.execute(query)
    # end transaction
    query = "COMMIT"
    cursor.execute(query)
    conn.commit()
    print("Group created")

def update_user_name():
    user_id = input("Enter the user ID: ")
    user_name = input("Enter the user name: ")
    cursor = conn.cursor()
    query = f"UPDATE user_table SET user_name = '{user_name}' WHERE user_id = {user_id}"
    cursor.execute(query)
    conn.commit()
    print("User name updated")

def update_group_name():
    group_id = input("Enter the group ID: ")
    group_name = input("Enter the group name: ")
    cursor = conn.cursor()
    query = f"UPDATE group_table SET group_name = '{group_name}' WHERE group_id = {group_id}"
    cursor.execute(query)
    conn.commit()
    print("Group name updated")

def remove_a_user_from_group():
    user_id = input("Enter the user ID: ")
    group_id = input("Enter the group ID: ")
    cursor = conn.cursor()
    query = f"DELETE FROM group_member WHERE user_id = {user_id} AND group_id = {group_id}"
    cursor.execute(query)
    conn.commit()
    print("User removed from group")

def block_a_user_from_one_user_contact_list():
    user_id = input("Enter the user ID: ")
    person_id = input("Enter the person ID: ")
    cursor = conn.cursor()
    query = f"UPDATE user_contacts SET isBlocked = 1 WHERE user_id = {user_id} AND person_id = {person_id}"
    cursor.execute(query)
    conn.commit()
    print("User blocked")

def delete_a_group():
    group_id = input("Enter the group ID: ")
    cursor = conn.cursor()
    query = f"DELETE FROM group_table WHERE group_id = {group_id}"
    cursor.execute(query)
    query = f"DELETE FROM group_member WHERE group_id = {group_id}"
    cursor.execute(query)
    conn.commit()
    print("Group deleted")

def delete_a_chat():
    user_id = input("Enter the user ID: ")
    person_id = input("Enter the person ID: ")
    cursor = conn.cursor()
    # begin transaction
    query = "BEGIN"
    cursor.execute(query)
    query = f"DELETE FROM user_contacts WHERE (user_id = {user_id} AND person_id = {person_id}) OR (user_id = {person_id} AND person_id = {user_id})"
    cursor.execute(query)
    query = f"DELETE FROM personal_message WHERE (sender_id = {user_id} AND receiver_id = {person_id}) OR (sender_id = {person_id} AND receiver_id = {user_id})"
    cursor.execute(query)
    # end transaction
    query = "COMMIT"
    cursor.execute(query)
    conn.commit()
    print("Chat deleted")

def promote_a_user_to_admin_in_a_group():
    user_id = input("Enter the user ID: ")
    group_id = input("Enter the group ID: ")
    cursor = conn.cursor()
    query = f"UPDATE group_member SET user_role = 'admin' WHERE user_id = {user_id} AND group_id = {group_id}"
    cursor.execute(query)
    conn.commit()
    print("User promoted to admin")

def search_for_a_keyword_in_all_chat_group_chat_messages():
    keyword = input("Enter the keyword: ")
    cursor = conn.cursor()
    # begin transaction
    query = "BEGIN"
    cursor.execute(query)
    query = f"SELECT * FROM personal_message WHERE message_text LIKE '%{keyword}%'"
    cursor.execute(query)
    message_list = cursor.fetchall()
    print(message_list)
    query = f"SELECT * FROM group_message WHERE message_text LIKE '%{keyword}%'"
    cursor.execute(query)
    # end transaction
    query = "COMMIT"
    cursor.execute(query)
    message_list = cursor.fetchall()
    print(message_list)

def delete_a_user_account():
    user_id = input("Enter the user ID: ")
    cursor = conn.cursor()
    # begin transaction
    query = "BEGIN"
    cursor.execute(query)
    query = f"DELETE FROM user_table WHERE user_id = {user_id}"
    cursor.execute(query)
    query = f"DELETE FROM user_contacts WHERE user_id = {user_id} OR person_id = {user_id}"
    cursor.execute(query)
    query = f"DELETE FROM personal_message WHERE sender_id = {user_id} OR receiver_id = {user_id}"
    cursor.execute(query)
    query = f"DELETE FROM group_member WHERE user_id = {user_id}"
    cursor.execute(query)
    query = f"DELETE FROM group_message WHERE sender_id = {user_id}"
    cursor.execute(query)
    query = f"DELETE FROM status_update WHERE user_id = {user_id}"
    cursor.execute(query)
    # end transaction
    query = "COMMIT"
    cursor.execute(query)
    conn.commit()
    print("User account deleted")

def mark_a_message_as_seen():
    message_id = input("Enter the message ID: ")
    cursor = conn.cursor()
    query = f"UPDATE personal_message SET seen = 1 WHERE message_id = {message_id}"
    cursor.execute(query)
    conn.commit()
    print("Message marked as seen")

def update_a_message():
    message_id = input("Enter the message ID: ")
    message_text = input("Enter the message text: ")
    cursor = conn.cursor()
    query = f"UPDATE personal_message SET message_text = '{message_text}' WHERE message_id = {message_id}"
    cursor.execute(query)
    conn.commit()
    print("Message updated")

def delete_a_message():
    message_id = input("Enter the message ID: ")
    cursor = conn.cursor()
    query = f"DELETE FROM personal_message WHERE message_id = {message_id}"
    cursor.execute(query)
    conn.commit()
    print("Message deleted")

def get_a_users_settings():
    user_id = input("Enter the user ID: ")
    cursor = conn.cursor()
    query = f"SELECT * FROM user_settings WHERE user_id = {user_id}"
    cursor.execute(query)
    user_settings = cursor.fetchall()
    print(user_settings)

def change_a_users_settings():
    user_id = input("Enter the user ID: ")
    sound_notification = input("Enter the sound notification: ")
    cursor = conn.cursor()
    query = f"UPDATE user_settings SET sound_notification = {sound_notification} WHERE user_id = {user_id}"
    cursor.execute(query)
    conn.commit()
    print("User settings updated")

def get_all_contacts_status():
    user_id = input("Enter the user ID: ")
    cursor = conn.cursor()
    query = f"SELECT * FROM status_update JOIN media ON status_update.status_media = media.media_id WHERE user_id IN (SELECT person_id FROM user_contacts WHERE user_id = {user_id})"
    cursor.execute(query)
    status_list = cursor.fetchall()
    print(status_list)

def delete_a_users_status():
    user_id = input("Enter the user ID: ")
    cursor = conn.cursor()
    query = f"DELETE FROM status_update WHERE user_id = {user_id}"
    cursor.execute(query)
    conn.commit()
    print("User status deleted")

def list_all_users_in_a_group():
    group_id = input("Enter the group ID: ")
    cursor = conn.cursor()
    query = f"SELECT * FROM group_member JOIN user_table ON group_member.user_id = user_table.user_id WHERE group_id = {group_id}"
    cursor.execute(query)
    user_list = cursor.fetchall()
    print(user_list)

def fetch_all_common_groups_between_2_users():
    user_id_1 = input("Enter the user ID 1: ")
    user_id_2 = input("Enter the user ID 2: ")
    cursor = conn.cursor()
    query = f"SELECT * FROM group_member WHERE group_id IN (SELECT group_id FROM group_member WHERE user_id = {user_id_1}) AND user_id = {user_id_2}"
    cursor.execute(query)
    group_list = cursor.fetchall()
    print(group_list)

def main():
    while True:
        print(
        """
        ###########################
        ## Project Topic - WhatsApp ##
        ###########################

        Welcome to WhatsApp Database!
        In this, you will interact with WhatsApp's common queries through this interface.
        Your quest starts now!

        """
    )
        inp = input("Press s to start: or q to quit: ")
        if inp.lower() == 's':
            print("1. Get user info by user id")
            print("2. Get user contact list by user id")
            print("3. Get all message for a chat with media")
            print("4. Get all message for a group with media")
            print("5. List all groups of a user")
            print("6. Get information of a group")
            print("7. Get last message of all personal chat of a user")
            print("8. Add a new user to a group")
            print("9. Send message to a user")
            print("10. Send message to a group")
            print("11. Begin a new chat")
            print("12. Create a new group")
            print("13. Update user name")
            print("14. Update group name")
            print("15. Remove a user from group")
            print("16. Block a user from one user contact list")
            print("17. Delete a group")
            print("18. Delete a chat")
            print("19. Promote a user to admin in a group")
            print("20. Search for a keyword in all chat/group chat messages")
            print("21. Delete a user account")
            print("22. Mark a message as seen")
            print("23. Update a message")
            print("24. Delete a message")
            print("25. Get a user's settings")
            print("26. Change a user's settings")
            print("27. Get all contacts status")
            print("28. Delete a user's status")
            print("29. List all users in a group")
            print("30. Fetch all common groups between 2 users")
            print("q. Quit")

            choice = input("Enter your choice (q to quit): ")

            if choice == '1':
                get_user_by_id()
            elif choice == '2':
                get_user_contact_list_by_id()
            elif choice == '3':
                get_all_message_for_a_chat_with_media()
            elif choice == '4':
                get_all_message_for_a_group_with_media()
            elif choice == '5':
                list_all_groups_of_a_user()
            elif choice == '6':
                get_information_of_a_group()
            elif choice == '7':
                get_last_message_of_all_personal_chat_of_a_user()
            elif choice == '8':
                add_a_new_user_to_a_group()
            elif choice == '9':
                send_message_to_a_user()
            elif choice == '10':
                send_message_to_a_group()
            elif choice == '11':
                begin_a_new_chat()
            elif choice == '12':
                create_a_new_group()
            elif choice == '13':
                update_user_name()
            elif choice == '14':
                update_group_name()
            elif choice == '15':
                remove_a_user_from_group()
            elif choice == '16':
                block_a_user_from_one_user_contact_list()
            elif choice == '17':
                delete_a_group()
            elif choice == '18':
                delete_a_chat()
            elif choice == '19':
                promote_a_user_to_admin_in_a_group()
            elif choice == '20':
                search_for_a_keyword_in_all_chat_group_chat_messages()
            elif choice == '21':
                delete_a_user_account()
            elif choice == '22':
                mark_a_message_as_seen()
            elif choice == '23':
                update_a_message()
            elif choice == '24':
                delete_a_message()
            elif choice == '25':
                get_a_users_settings()
            elif choice == '26':
                change_a_users_settings()
            elif choice == '27':
                get_all_contacts_status()
            elif choice == '28':
                delete_a_users_status()
            elif choice == '29':
                list_all_users_in_a_group()
            elif choice == '30':
                fetch_all_common_groups_between_2_users()
            elif choice.lower() == 'q':
                break
            else:
                print("Invalid choice")
        elif inp.lower() == 'q':
            break
main()
conn.close()
