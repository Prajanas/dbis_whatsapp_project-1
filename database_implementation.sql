CREATE DATABASE whatsapp;
USE whatsapp;

CREATE TABLE media
(
  media_id INT NOT NULL,
  media_type VARCHAR(20) NOT NULL,
  media_url VARCHAR(800) NOT NULL,
  PRIMARY KEY (media_id)
);

CREATE TABLE user_table
(
  user_id INT NOT NULL,
  user_name VARCHAR(20) NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  profile_picture INT,
  user_status VARCHAR(20) NOT NULL,
  user_about VARCHAR(400),
  last_seen BOOLEAN NOT NULL,
  PRIMARY KEY (user_id),
  FOREIGN KEY (profile_picture) REFERENCES media(media_id)
);

CREATE TABLE user_settings
(
  user_id INT NOT NULL,
  sound_notification BOOLEAN NOT NULL,
  last_seen_visibility BOOLEAN NOT NULL,
  profile_picture_visibility BOOLEAN NOT NULL,
  read_receipt BOOLEAN NOT NULL,
  dark_mode BOOLEAN NOT NULL,
  app_language VARCHAR(20) NOT NULL,
  PRIMARY KEY (user_id),
  FOREIGN KEY (user_id) REFERENCES user_table(user_id)
);

CREATE TABLE group_member
(
  user_id INT NOT NULL,
  group_id INT NOT NULL,
  user_role VARCHAR(20) NOT NULL,
  joined_date DATE NOT NULL,
  PRIMARY KEY (user_id, group_id),
  FOREIGN KEY (user_id) REFERENCES user_table(user_id)
);

CREATE TABLE personal_message
(
  message_id INT NOT NULL,
  sender_id INT NOT NULL,
  receiver_id INT NOT NULL,
  last_update DATE NOT NULL,
  created_at DATE NOT NULL,
  message_text VARCHAR(800),
  message_media INT,
  seen BOOLEAN NOT NULL,
  delivered BOOLEAN NOT NULL,
  PRIMARY KEY (message_id),
  FOREIGN KEY (sender_id) REFERENCES user_table(user_id),
  FOREIGN KEY (receiver_id) REFERENCES user_table(user_id),
  FOREIGN KEY (message_media) REFERENCES media(media_id)
);

CREATE TABLE user_contacts
(
  user_id INT NOT NULL,
  person_id INT NOT NULL,
  person_name VARCHAR(20) NOT NULL,
  isBlocked BOOLEAN NOT NULL,
  PRIMARY KEY (user_id, person_id),
  FOREIGN KEY (user_id) REFERENCES user_table(user_id),
  FOREIGN KEY (person_id) REFERENCES user_table(user_id)
);

CREATE TABLE group_table
(
  group_id INT NOT NULL,
  group_name VARCHAR(20) NOT NULL,
  group_picture INT,
  creation_date DATE NOT NULL,
  group_description VARCHAR(400),
  PRIMARY KEY (group_id),
  FOREIGN KEY (group_picture) REFERENCES media(media_id)
);

CREATE TABLE status_update
(
  status_id INT NOT NULL,
  user_id INT NOT NULL,
  status_media INT,
  status_text VARCHAR(800) NOT NULL,
  last_update DATE NOT NULL,
  PRIMARY KEY (status_id),
  FOREIGN KEY (user_id) REFERENCES user_table(user_id),
  FOREIGN KEY (status_media) REFERENCES media(media_id)
);

CREATE TABLE group_message
(
  message_id INT NOT NULL,
  sender_id INT NOT NULL,
  group_id INT NOT NULL,
  last_update DATE NOT NULL,
  created_at DATE NOT NULL,
  message_text VARCHAR(800) NOT NULL,
  message_media INT,
  PRIMARY KEY (message_id),
  FOREIGN KEY (group_id) REFERENCES group_table(group_id),
  FOREIGN KEY (sender_id) REFERENCES user_table(user_id),
  FOREIGN KEY (message_media) REFERENCES media(media_id)
);
