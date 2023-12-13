import psycopg2
from prettytable import PrettyTable

def heading(title):
    print('-' * 60)
    print("** %s:" % title)
    print('-' * 60, '\n')

heading("User Story #7 Track Video Comments")
print("Testing for Video ID: 1")

us = '''
* Complex & Analytical US
   As a:  Creator
 I want:  To view comments on videos I made
So That:  I can see the opinion of viewers on the videos I made
'''

SHOW_CMD = True

def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))

def print_rows(rows):
    table = PrettyTable()
    table.field_names = ["Video ID", "Comment Text", "Comment Time", "User Name"]
    for row in rows:
        table.add_row(row)
    print(table)

def get_video_comments(video_id):
    print("This function retrieves and displays comments on a specific video.")

    tmpl = '''
    SELECT Vi.video_id, C.comment_text, C.comment_time, U.user_name
      FROM Comment C
      JOIN Videos Vi ON Vi.video_id = C.video_id
      JOIN Viewer V ON C.viewer_id = V.viewer_id
      JOIN Users U ON V.viewer_id = U.user_id
     WHERE C.video_id = %s
     ORDER BY C.comment_time DESC;

    '''
    cur = conn.cursor()
    cur.execute(tmpl, (video_id,))
    rows = cur.fetchall()
    print_rows(rows)
    cur.close()

if __name__ == '__main__':
    try:
        db, user = 'project', 'isdb'
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True

        print(us)
        get_video_comments(1)
        conn.close()
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))
    except Exception as e:
        print("An error occurred: %s" % (e,))
