-- 1) Get user info by user id
SELECT * FROM user_table WHERE user_id = 1;

-- 2) Get user contact list by user id
SELECT * FROM user_contacts WHERE user_id = 1;

-- 3) Retreive all message for a chat with media
SELECT * FROM personal_message JOIN media ON personal_message.message_media = media.media_id WHERE (sender_id = 1 AND receiver_id = 2) OR (sender_id = 2 AND receiver_id = 1);

-- 4) Retreive all message for a group with media
SELECT * FROM group_message JOIN media ON group_message.message_media = media.media_id WHERE group_id = 1;

-- 5) List all groups of a user
SELECT * FROM group_member JOIN group_table ON group_member.group_id = group_table.group_id WHERE user_id = 1;

-- 6) Get information of a group
SELECT * FROM group_table JOIN media ON group_table.group_picture = media.media_id WHERE group_id = 1;

-- 7) Get last message of all personal chat of a user
SELECT * FROM personal_message WHERE (sender_id = 1 OR receiver_id = 1);

-- 8) Add a new user to a group
INSERT INTO group_member (user_id, group_id, user_role, joined_date) VALUES (1, 1, 'member', '2020-01-01');

-- 9) Send message to a user
INSERT INTO media (media_id, media_type, media_url) VALUES (11, 'image', 'https://www.google.com');

INSERT INTO personal_message (message_id, sender_id, receiver_id, last_update, created_at, message_text, message_media) VALUES (21, 1, 2, '2020-01-01', '2020-01-01', 'Hello', 11);

-- 10) Send message to a group
INSERT INTO media (media_id, media_type, media_url) VALUES (12, 'image', 'https://www.google.com');

INSERT INTO group_message (message_id, sender_id, group_id, last_update, created_at, message_text, message_media) VALUES (21, 1, 1, '2020-01-01', '2020-01-01', 'Hello', 12);

-- 11) Begin a new chat
INSERT INTO user_contacts (user_id, person_id, person_name, isBlocked) VALUES (5, 2, 'John', 0);

-- 12) Create a new group
INSERT INTO media (media_id, media_type, media_url) VALUES (13, 'image', 'https://www.google.com');

INSERT INTO group_table (group_id, group_name, group_picture, creation_date, group_description) VALUES (6, 'Group 6', 13, '2020-01-01', 'Group 6 des');

-- 13) Update user info
UPDATE user_table SET user_name = 'John' WHERE user_id = 1;

-- 14) update group info
UPDATE group_table SET group_name = 'Group 6' WHERE group_id = 6;

-- 15) Remove a user from group
DELETE FROM group_member WHERE user_id = 1 AND group_id = 1;

-- 16) Block a user from one user's contact list
UPDATE user_contacts SET isBlocked = 1 WHERE user_id = 1 AND person_id = 2;

-- 17) Delete a group
DELETE FROM group_table WHERE group_id = 6;
DELETE FROM group_member WHERE group_id = 6;

-- 18) Delete a chat
DELETE FROM user_contacts WHERE (user_id = 1 AND person_id = 2) OR (user_id = 2 AND person_id = 1);
DELETE FROM personal_message WHERE (sender_id = 1 AND receiver_id = 2) OR (sender_id = 2 AND receiver_id = 1);

-- 19) Promote a user to admin in a group
UPDATE group_member SET user_role = 'admin' WHERE user_id = 1 AND group_id = 1;

-- 20) Search for a keyword in all chat + group chat messages
SELECT * FROM personal_message WHERE message_text LIKE '%hello%';
SELECT * FROM group_message WHERE message_text LIKE '%hello%';

-- 21) Delete a user account
DELETE FROM user_table WHERE user_id = 1;
DELETE FROM user_contacts WHERE user_id = 1 OR person_id = 1;
DELETE FROM personal_message WHERE sender_id = 1 OR receiver_id = 1;
DELETE FROM group_member WHERE user_id = 1;
DELETE FROM group_message WHERE sender_id = 1;
DELETE FROM status_update WHERE user_id = 1;

-- 22) Mark a message as seen
UPDATE personal_message SET seen = 1 WHERE message_id = 1;

-- 23) Update a message
UPDATE personal_message SET message_text = 'Hello' WHERE message_id = 1;

-- 24) Delete a message
DELETE FROM personal_message WHERE message_id = 1;

-- 25) Get a users's settings 
SELECT * FROM user_settings WHERE user_id = 1;

-- 26) Change a user's settings
UPDATE user_settings SET sound_notification = 1 WHERE user_id = 1;

-- 27) Get all contacts status
SELECT * FROM status_update JOIN media ON status_update.status_media = media.media_id WHERE user_id IN (SELECT person_id FROM user_contacts WHERE user_id = 1);

-- 28) Delete a user's status
DELETE FROM status_update WHERE user_id = 1;

-- 29) List all users in a group
SELECT * FROM group_member JOIN user_table ON group_member.user_id = user_table.user_id WHERE group_id = 1;

-- 30) Fetch all common groups between 2 users
SELECT * FROM group_member WHERE group_id IN (SELECT group_id FROM group_member WHERE user_id = 1) AND user_id = 2;
