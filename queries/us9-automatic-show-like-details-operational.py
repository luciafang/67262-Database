import psycopg2
from prettytable import PrettyTable

def heading(str):
    print('-' * 60)
    print("** %s:" % str)
    print('-' * 60, '\n')

heading("User Story #9: Automatic show likes details")

us = '''
* Simple US
   As a:  Creator
 I want:  To see when my videos are being liked 
So That:  I know when my fans are checking my videos. 
'''

SHOW_CMD = True

def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))

def print_rows(rows):
    table = PrettyTable()
    table.field_names = ["Like ID", "Viewer ID", "Video ID", "Like Time"]
    for row in rows:
        table.add_row(row)
    print(table)

def fetch_likes():
    cur.execute('SELECT like_id, viewer_id, video_id, like_time FROM "Like"')
    rows = cur.fetchall()
    print_rows(rows)

def add_like(like_id, viewer_id, video_id):
    print("This function fetches details of when the video is being liked and being liked by whom.")

    tmpl = '''
        CREATE OR REPLACE FUNCTION auto_fill_like_time()
        RETURNS TRIGGER 
        LANGUAGE plpgsql AS
        $$
        BEGIN
            NEW.like_time := current_timestamp;
            RETURN NEW;
        END;
        $$;

        DROP TRIGGER IF EXISTS tr_fill_like_time ON "Like";

        CREATE TRIGGER tr_fill_like_time
            BEFORE INSERT ON "Like"
            FOR EACH ROW
            EXECUTE FUNCTION auto_fill_like_time();

        INSERT INTO "Like"(like_id, viewer_id, video_id) 
            VALUES (%s, %s, %s);
    '''
    cmd = cur.mogrify(tmpl, (like_id, viewer_id, video_id))
    cur.execute(cmd)

if __name__ == '__main__':
    try:
        db, user = 'project', 'isdb'
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()

        print(us)


        print("Likes table before operation:")
        fetch_likes()

        print("\nTesting by liking video 3 by viewer 2")
        add_like(29, 2, 3)

        print("\nLikes table after operation:")
        fetch_likes()

    except psycopg2.Error as e:
        print("Unable to open connection: %s" % e)
