import psycopg2
from prettytable import PrettyTable


def heading(str):
    print('-' * 60)
    print("** %s:" % str)
    print('-' * 60, '\n')

heading("User Story #4 Video Recommendations for Viewers")
print("Testing for Viewer ID: 3")

us = '''
* Complex & Analytical US
   As a:  Viewer
 I want:  The system to recommend me videos based on my likes and comments
So That:  I can discover more content that tailors to my interests.
'''

SHOW_CMD = True


def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))


def print_rows(rows):
    table = PrettyTable()
    table.field_names = ["Video ID", "Creator Name", "Like Count"]
    for row in rows:
        table.add_row(row)
    print(table)


def get_video_recommendations(viewer_id):
    print("This function recommends videos to a specific viewer based on their likes.")

    tmpl = '''
    SELECT V.video_id, U.user_name AS creator_name, COUNT(L.like_id) AS like_count
      FROM "Like" L
      JOIN Videos V ON V.video_id = L.video_id
      JOIN Creator C ON V.creator_id = C.creator_id
      JOIN Users U ON C.creator_id = U.user_id
     WHERE L.viewer_id = %s
     GROUP BY V.video_id, U.user_name
     ORDER BY like_count DESC;
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
        get_video_recommendations(3)
        conn.close()
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))
    except Exception as e:
        print("An error occurred: %s" % (e,))
