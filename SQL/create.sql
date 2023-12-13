-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2023-12-08 20:27:34.474

-- tables
-- Table: Advertiser
CREATE TABLE Advertiser (
    advertiser_id int  NOT NULL,
    CONSTRAINT Advertiser_pk PRIMARY KEY (advertiser_id)
);

-- Table: Comment
CREATE TABLE Comment (
    comment_id int  NOT NULL,
    viewer_id int  NOT NULL,
    video_id int  NOT NULL,
    comment_text text  NOT NULL,
    comment_time timestamp  NOT NULL,
    CONSTRAINT Comment_pk PRIMARY KEY (comment_id)
);

-- Table: Creator
CREATE TABLE Creator (
    creator_id int  NOT NULL,
    CONSTRAINT Creator_pk PRIMARY KEY (creator_id)
);

-- Table: Like
CREATE TABLE "Like" (
    like_id int  NOT NULL,
    viewer_id int  NOT NULL,
    video_id int  NOT NULL,
    like_time timestamp  NOT NULL,
    CONSTRAINT Like_pk PRIMARY KEY (like_id)
);

-- Table: Livestream
CREATE TABLE Livestream (
    livestream_id int  NOT NULL,
    creator_id int  NOT NULL,
    viewer_id int  NOT NULL,
    start_time timestamp  NOT NULL,
    end_time timestamp  NOT NULL,
    CONSTRAINT Livestream_pk PRIMARY KEY (livestream_id)
);

-- Table: Money
CREATE TABLE Money (
    video_id int  NOT NULL,
    amount int  NOT NULL,
    account_id int  NOT NULL,
    CONSTRAINT Money_pk PRIMARY KEY (account_id)
);

-- Table: Saved_videos
CREATE TABLE Saved_videos (
    saved_id int  NOT NULL,
    viewer_id int  NOT NULL,
    video_id int  NOT NULL,
    CONSTRAINT Saved_videos_pk PRIMARY KEY (saved_id)
);

-- Table: Users
CREATE TABLE Users (
    user_id int  NOT NULL,
    user_name text  NOT NULL,
    CONSTRAINT Users_pk PRIMARY KEY (user_id)
);

-- Table: Videos
CREATE TABLE Videos (
    video_id int  NOT NULL,
    duration int  NOT NULL,
    upload_time timestamp  NOT NULL,
    hashtag text  NOT NULL,
    is_advertisement boolean  NOT NULL,
    advertiser_id int  NOT NULL,
    creator_id int  NOT NULL,
    viewer_id int  NOT NULL,
    CONSTRAINT Videos_pk PRIMARY KEY (video_id)
);

-- Table: Viewer
CREATE TABLE Viewer (
    viewer_id int  NOT NULL,
    content_type boolean  NOT NULL,
    content_id int  NOT NULL,
    CONSTRAINT Viewer_pk PRIMARY KEY (viewer_id)
);

-- foreign keys
-- Reference: Advertiser_User (table: Advertiser)
ALTER TABLE Advertiser ADD CONSTRAINT Advertiser_User
    FOREIGN KEY (advertiser_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Comment_Videos (table: Comment)
ALTER TABLE Comment ADD CONSTRAINT Comment_Videos
    FOREIGN KEY (video_id)
    REFERENCES Videos (video_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Comment_Viewer (table: Comment)
ALTER TABLE Comment ADD CONSTRAINT Comment_Viewer
    FOREIGN KEY (viewer_id)
    REFERENCES Viewer (viewer_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Creator_User (table: Creator)
ALTER TABLE Creator ADD CONSTRAINT Creator_User
    FOREIGN KEY (creator_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Like_Videos (table: Like)
ALTER TABLE "Like" ADD CONSTRAINT Like_Videos
    FOREIGN KEY (video_id)
    REFERENCES Videos (video_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Like_Viewer (table: Like)
ALTER TABLE "Like" ADD CONSTRAINT Like_Viewer
    FOREIGN KEY (viewer_id)
    REFERENCES Viewer (viewer_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Livestream_Creator (table: Livestream)
ALTER TABLE Livestream ADD CONSTRAINT Livestream_Creator
    FOREIGN KEY (creator_id)
    REFERENCES Creator (creator_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Livestream_Viewer (table: Livestream)
ALTER TABLE Livestream ADD CONSTRAINT Livestream_Viewer
    FOREIGN KEY (viewer_id)
    REFERENCES Viewer (viewer_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Money_Videos (table: Money)
ALTER TABLE Money ADD CONSTRAINT Money_Videos
    FOREIGN KEY (video_id)
    REFERENCES Videos (video_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Saved_videos_Videos (table: Saved_videos)
ALTER TABLE Saved_videos ADD CONSTRAINT Saved_videos_Videos
    FOREIGN KEY (video_id)
    REFERENCES Videos (video_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Saved_videos_Viewer (table: Saved_videos)
ALTER TABLE Saved_videos ADD CONSTRAINT Saved_videos_Viewer
    FOREIGN KEY (viewer_id)
    REFERENCES Viewer (viewer_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Videos_Advertiser (table: Videos)
ALTER TABLE Videos ADD CONSTRAINT Videos_Advertiser
    FOREIGN KEY (advertiser_id)
    REFERENCES Advertiser (advertiser_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Videos_Creator (table: Videos)
ALTER TABLE Videos ADD CONSTRAINT Videos_Creator
    FOREIGN KEY (creator_id)
    REFERENCES Creator (creator_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Videos_Viewer (table: Videos)
ALTER TABLE Videos ADD CONSTRAINT Videos_Viewer
    FOREIGN KEY (viewer_id)
    REFERENCES Viewer (viewer_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Viewer_Users (table: Viewer)
ALTER TABLE Viewer ADD CONSTRAINT Viewer_Users
    FOREIGN KEY (viewer_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

