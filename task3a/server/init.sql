CREATE TABLE users (
id SERIAL PRIMARY KEY,
username VARCHAR(50) UNIQUE NOT NULL,
password TEXT NOT NULL
);

INSERT INTO users (username, password) VALUES
('admin', '$2b$12$W4m1sATx9BpISy5UAyr9Xu1bLhDOxz/rNXuYD8BXWMGsQSgpKsuzO');

CREATE TABLE tracks (
song_id SERIAL PRIMARY KEY,
artist VARCHAR(100),
genre VARCHAR(100),
file_path VARCHAR(500) NOT NULL,
title VARCHAR(100)
);

INSERT INTO tracks (artist, genre, file_path, title) VALUES
('Ravi Basrur', 'Soundtrack', '/music/kgf.mp3', 'KGF'),
('Various Artists', 'Classical', '/music/raga_of_revenge.mp3', 'Raga of Revenge'),
('Unknown', 'General', '/music/music1.mp3', 'Music 1'),
('Boney M', 'Pop', '/music/rasputin.mp3', 'Rasputin');

CREATE TABLE playlists (
playlist_id SERIAL PRIMARY KEY,
user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
playlist_name VARCHAR(100)
);

CREATE TABLE playlist_songs (
playlist_id INTEGER REFERENCES playlists(playlist_id) ON DELETE CASCADE,
song_id INTEGER REFERENCES tracks(song_id) ON DELETE CASCADE,
PRIMARY KEY (playlist_id, song_id)
);

CREATE TABLE history (
history_id SERIAL PRIMARY KEY,
user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
song_id INTEGER NOT NULL REFERENCES tracks(song_id) ON DELETE CASCADE,
played_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE login_attempts (
username TEXT,
ip_address TEXT,
failed_attempts INTEGER DEFAULT 0,
last_attempt TIMESTAMP
);

CREATE TABLE active_bans (
ban_id SERIAL PRIMARY KEY,
ip TEXT NOT NULL,
reason TEXT NOT NULL,
banned_at TIMESTAMP NOT NULL,
expires_at TIMESTAMP
);


