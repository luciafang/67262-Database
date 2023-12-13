\c project;


\echo "Table: Users";
SELECT * FROM Users;

\echo "Table: Users identified as Viewer";
SELECT * FROM Viewer;

\echo "Table: Users identified as Advertiser";
SELECT * FROM Advertiser;

\echo "Table: Users identified as Creator";
SELECT * FROM Creator;

\echo "Table: all the videos on Tiktok";
SELECT * FROM Videos;

\echo "Table: all the comments make on Tiktok";
SELECT * FROM Comment;

\echo "Table: all the likes clicked on Tiktok";
SELECT * FROM "Like";

\echo "Table: all the livestreams made on Tiktok";
SELECT * FROM LiveStream;

\echo "Table: all the Money made by creators on Tiktok";
SELECT * FROM Money;

\echo "Table: all the saved videos";
SELECT * FROM Saved_videos;