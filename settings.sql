DROP DATABASE IF EXISTS supreme_like;
CREATE DATABASE supreme_like;
CREATE USER supreme_like_user WITH PASSWORD 'admin';
GRANT ALL PRIVILEGES ON DATABASE supreme_like TO supreme_like_user;