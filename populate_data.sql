-- Inserting data into media (message_media)
INSERT INTO media (media_id, media_type, media_url)
VALUES
(1, 'image', 'https://yourdomain.com/images/image1.jpg'),
(2, 'video', 'https://yourdomain.com/videos/video1.mp4'),
(3, 'image', 'https://yourdomain.com/images/image2.png'),
(4, 'image', 'https://yourdomain.com/images/image3.jpg'),
(5, 'video', 'https://yourdomain.com/videos/video2.mp4'),
(6, 'image', 'https://yourdomain.com/images/image4.png'),
(7, 'video', 'https://yourdomain.com/videos/video3.mp4'),
(8, 'image', 'https://yourdomain.com/images/image5.jpg'),
(9, 'image', 'https://yourdomain.com/images/image6.png'),
(10, 'video', 'https://yourdomain.com/videos/video4.mp4');

-- Inserting data into user_table
INSERT INTO user_table (user_id, user_name, phone_number, profile_picture, user_status, user_about, last_seen)
VALUES
(1, 'Alice', '+1234567890', 1, 'Available', 'Hey there! I love chatting.', true),
(2, 'Bob', '+1987654321', 2, 'Busy', 'Busy with work.', false),
(3, 'Charlie', '+1112223333', 3, 'Available', 'Lets connect!', true),
(4, 'David', '+4445556666', 4, 'Away', 'Out for a vacation.', false),
(5, 'Eva', '+7778889999', 5, 'Available', 'Enjoying life!', true),
(6, 'Frank', '+6665554444', 6, 'Busy', 'In a meeting.', false),
(7, 'Grace', '+3332221111', 7, 'Available', 'Music lover.', true),
(8, 'Hannah', '+9998887777', 8, 'Away', 'Taking a break.', false),
(9, 'Ian', '+5556667777', 9, 'Available', 'Exploring new things.', true),
(10, 'Jack', '+1231231234', 10, 'Busy', 'Focused on studies.', false),
(11, 'Katherine', '+3213214321', 3, 'Available', 'Bookworm alert!', true),
(12, 'Liam', '+9991113332', 4, 'Away', 'Gone for a walk.', false);

-- Inserting data into user_settings
INSERT INTO user_settings (user_id, sound_notification, last_seen_visibility, profile_picture_visibility, read_receipt, dark_mode, app_language)
VALUES
(1, true, true, true, true, true, 'English'),
(2, true, true, false, true, false, 'Spanish'),
(3, true, true, true, true, true, 'French'),
(4, false, true, true, false, false, 'Hindi'),
(5, true, true, true, true, true, 'German'),
(6, false, true, false, false, false, 'English'),
(7, true, true, true, true, true, 'English'),
(8, false, true, true, false, false, 'Hindi'),
(9, true, true, true, true, true, 'English'),
(10, true, true, false, true, false, 'English'),
(11, true, true, true, true, true, 'French'),
(12, false, true, true, false, false, 'English');

-- Inserting data into user_contacts
INSERT INTO user_contacts (user_id, person_id, person_name, isBlocked)
VALUES
(1, 2, 'Bob', false),
(1, 3, 'Charlie', false),
(1, 4, 'David', true),
(1, 5, 'Eva', false),
(1, 6, 'Frank', true),
(2, 1, 'Alice', false),
(2, 3, 'Charlie', true),
(2, 4, 'David', false),
(2, 5, 'Eva', false),
(2, 7, 'Grace', false),
(3, 1, 'Alice', false),
(3, 2, 'Bob', false),
(3, 4, 'David', true),
(3, 6, 'Frank', false),
(3, 7, 'Grace', true),
(4, 1, 'Alice', true),
(4, 2, 'Bob', false),
(4, 3, 'Charlie', false),
(4, 5, 'Eva', true),
(4, 6, 'Frank', false);

-- Inserting data into group_member
INSERT INTO group_member (user_id, group_id, user_role, joined_date)
VALUES
(1, 1, 'Admin', '2023-01-10'),
(2, 1, 'Member', '2023-02-15'),
(3, 1, 'Member', '2023-02-15'),
(4, 1, 'Admin', '2023-01-20'),
(5, 1, 'Member', '2023-03-01'),
(1, 2, 'Admin', '2023-02-01'),
(2, 2, 'Member', '2023-02-01'),
(3, 2, 'Member', '2023-02-01'),
(4, 2, 'Admin', '2023-02-01'),
(5, 2, 'Member', '2023-02-01'),
(6, 2, 'Member', '2023-02-01'),
(7, 2, 'Member', '2023-02-01'),
(8, 2, 'Member', '2023-02-01'),
(9, 2, 'Member', '2023-02-01'),
(10, 2, 'Member', '2023-02-01'),
(11, 2, 'Member', '2023-02-01'),
(12, 2, 'Member', '2023-02-01'),
(2, 3, 'Admin', '2023-03-10'),
(4, 3, 'Member', '2023-03-10'),
(6, 3, 'Member', '2023-03-10');

-- Inserting data into personal_message
INSERT INTO personal_message (message_id, sender_id, receiver_id, last_update, created_at, message_text, message_media, seen, delivered)
VALUES
(1, 1, 2, '2023-01-01', '2023-01-01', 'Hey, how are you?', NULL, 1, 1),
(2, 2, 1, '2023-01-01', '2023-01-01', 'Im good, thanks!', 1, 1, 1),
(3, 3, 1, '2023-01-02', '2023-01-02', 'Whats up?', NULL, 0, 1),
(4, 1, 3, '2023-01-02', '2023-01-02', 'Not much, just chilling.', NULL, 1, 1),
(5, 2, 3, '2023-01-03', '2023-01-03', 'Lets catch up soon!', 2, 0, 1),
(6, 3, 2, '2023-01-03', '2023-01-03', 'Definitely!', NULL, 0, 0),
(7, 4, 5, '2023-01-04', '2023-01-04', 'How have you been?', NULL, 0, 0),
(8, 5, 4, '2023-01-04', '2023-01-04', 'Ive been busy with work.', 3, 0, 0),
(9, 6, 5, '2023-01-05', '2023-01-05', 'Long time no see!', NULL, 0, 0),
(10, 5, 6, '2023-01-05', '2023-01-05', 'I know, we should hang out.', NULL, 0, 0),
(11, 7, 8, '2023-01-06', '2023-01-06', 'What are your plans for the weekend?', NULL, 0, 0),
(12, 8, 7, '2023-01-06', '2023-01-06', 'Thinking of a movie night.', 4, 0, 0),
(13, 9, 10, '2023-01-07', '2023-01-07', 'Any recommendations for a good book?', NULL, 0, 0),
(14, 10, 9, '2023-01-07', '2023-01-07', 'How about some classic literature?', 5, 0, 0),
(15, 11, 12, '2023-01-08', '2023-01-08', 'Planning any trips?', NULL, 0, 0),
(16, 12, 11, '2023-01-08', '2023-01-08', 'Yes, exploring some hiking trails.', NULL, 0, 0),
(17, 1, 4, '2023-01-09', '2023-01-09', 'We should hang out sometime.', NULL, 0, 0),
(18, 4, 1, '2023-01-09', '2023-01-09', 'Definitely! Lets plan something.', NULL, 0, 0),
(19, 2, 5, '2023-01-10', '2023-01-10', 'Do you have any travel plans?', NULL, 0, 0),
(20, 5, 2, '2023-01-10', '2023-01-10', 'Not yet, but Im thinking of a beach trip.', 6, 0, 0);

-- Inserting data into group_table
INSERT INTO group_table (group_id, group_name, group_picture, creation_date, group_description)
VALUES
(1, 'Tech Enthusiasts', 1, '2023-01-05', 'Discussions about the latest tech trends.'),
(2, 'Travel Lovers', 2, '2023-02-10', 'Sharing travel experiences and tips.'),
(3, 'Book Club', 3, '2023-03-15', 'Reading and discussing books.'),
(4, 'Birthday Planners', 4, '2023-04-20', 'Organizing surprise birthday parties.'),
(5, 'Event Management', 5, '2023-05-25', 'Planning and managing events.');

-- Inserting data into group_message
INSERT INTO group_message (message_id, sender_id, group_id, last_update, created_at, message_text, message_media)
VALUES
(1, 1, 1, '2023-10-10', '2023-10-10', 'Hello everyone!', 1),
(2, 2, 1, '2023-10-10', '2023-10-10', 'Good morning!', NULL),
(3, 3, 1, '2023-10-10', '2023-10-10', 'How is everyone doing today?', 2),
(4, 4, 1, '2023-10-11', '2023-10-11', 'Im excited about the upcoming event.', NULL),
(5, 1, 2, '2023-10-12', '2023-10-12', 'Welcome to the new group!', 3),
(6, 3, 2, '2023-10-12', '2023-10-12', 'Glad to be here!', NULL),
(7, 5, 2, '2023-10-12', '2023-10-12', 'Any plans for the weekend?', NULL),
(8, 2, 3, '2023-10-13', '2023-10-13', 'Lets discuss the project details.', 4),
(9, 4, 3, '2023-10-13', '2023-10-13', 'I have some suggestions.', NULL),
(10, 6, 3, '2023-10-13', '2023-10-13', 'We should start working on it soon.', 5),
(11, 1, 4, '2023-10-14', '2023-10-14', 'Happy birthday to our group member!', 6),
(12, 3, 4, '2023-10-14', '2023-10-14', 'Best wishes!', NULL),
(13, 5, 4, '2023-10-14', '2023-10-14', 'Lets celebrate!', NULL),
(14, 7, 4, '2023-10-15', '2023-10-15', 'Ill arrange a surprise party.', 7),
(15, 2, 5, '2023-10-16', '2023-10-16', 'Discussing the upcoming event details.', 8),
(16, 4, 5, '2023-10-16', '2023-10-16', 'Who will manage the decorations?', NULL),
(17, 6, 5, '2023-10-16', '2023-10-16', 'We need volunteers for the event.', 9),
(18, 8, 5, '2023-10-16', '2023-10-16', 'I can help with the arrangements.', NULL),
(19, 10, 5, '2023-10-17', '2023-10-17', 'Lets decide the schedule.', 10),
(20, 12, 5, '2023-10-17', '2023-10-17', 'Ill take care of the logistics.', NULL);

-- Inserting data into status_update
INSERT INTO status_update (status_id, user_id, status_media, status_text, last_update)
VALUES
(1, 1, 1, 'Feeling happy today!', '2023-01-01'),
(2, 2, 2, 'Enjoying the weekend vibes.', '2023-01-02'),
(3, 3, 3, 'Exploring new adventures!', '2023-01-03'),
(4, 4, NULL, 'Taking some time off.', '2023-01-04'),
(5, 5, 4, 'Music is my therapy.', '2023-01-05'),
(6, 6, 5, 'Feeling productive today!', '2023-01-06'),
(7, 7, 6, 'Celebrating a special day!', '2023-01-07'),
(8, 8, 7, 'Movie night with friends!', '2023-01-08'),
(9, 9, 8, 'Exploring the city streets.', '2023-01-09'),
(10, 10, 9, 'Prepping for an upcoming event.', '2023-01-10');
