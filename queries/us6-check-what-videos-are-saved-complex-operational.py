import psycopg2
from prettytable import PrettyTable

def heading(title):
    print('-' * 60)
    print(f"** {title}:")
    print('-' * 60, '\n')

heading("User Story: Check What Videos are in Saved Videos for that viewer")
print("Checking for Viewer ID: 2")

us = '''
* Complex US
   As a:  Viewer
 I want:  To check whether the video is in my Saved_videos
So That:  I can easily revisit content that resonates with me.
'''

SHOW_CMD = True

def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))

def print_rows(rows):
    table = PrettyTable()
    table.field_names = ["Viewer ID", "Video ID", "Upload Time", "Hashtag"]
    for row in rows:
        table.add_row(row)
    print(table)

def fetch_saved_video_details(viewer_id):
    print("This function checks what videos are saved by the viewer.")

    tmpl = '''
        SELECT S.viewer_id, S.video_id, V.upload_time, V.hashtag
        FROM Saved_videos S
        JOIN Videos V ON S.video_id = V.video_id
        WHERE S.viewer_id = %s;
    '''

    cur = conn.cursor()
    cur.execute(tmpl, (viewer_id,))
    rows = cur.fetchall()


    print_rows(rows)
    cur.close()

if __name__ == '__main__':
    try:
        db, user = 'project', 'isdb'
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        print(us)
        fetch_saved_video_details(2)
        conn.close()

    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))
