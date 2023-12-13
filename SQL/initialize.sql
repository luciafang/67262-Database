-- drop the trax database if it exists
DROP database if EXISTS project;

-- create it afresh
CREATE database project;
\c project

-- CREATE TYPE User_Type AS ENUM('customer', 'developer', 'manager');
-- CREATE TYPE Severity_Type AS ENUM( 'blocker', 'critical', 'major', 'normal', 'minor', 'trivial');
-- CREATE TYPE Status_Type AS ENUM( 'unconfirmed', 'new', 'assigned', 'reopened', 'resolved', 'verified', 'closed' );

\i create.SQL

-- load the data

\copy Users(user_id, user_name) FROM data/Users.csv csv header;
\copy Viewer(viewer_id, content_type, content_id) FROM data/Viewer.csv csv header;
\copy Advertiser(advertiser_id) FROM data/Advertiser.csv csv header;
\copy Creator(creator_id) FROM data/Creator.csv csv header;
\copy Videos(video_id, duration, upload_time, hashtag, is_advertisement, advertiser_id, creator_id, viewer_id) FROM data/Videos.csv csv header;
\copy Comment(comment_id, viewer_id, video_id, comment_text, comment_time) FROM data/Comment.csv csv header;
\copy "Like"(like_id, viewer_id, video_id, like_time) FROM data/Like.csv csv header;
\copy Livestream(livestream_id, creator_id, viewer_id, start_time, end_time) FROM data/Livestream.csv csv header;
\copy Money(video_id, amount, account_id) FROM data/Money.csv csv header;
\copy Saved_videos(saved_id, viewer_id, video_id) FROM data/Saved_videos.csv csv header;



