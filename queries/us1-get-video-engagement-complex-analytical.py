import psycopg2
from prettytable import PrettyTable

def heading(str):
    print('-' * 60)
    print("** %s:" % str)
    print('-' * 60, '\n')
    
heading("User Story #1 Track Video Engagement")
print("Testing for Creator ID: 6")

us = '''
* Complex & Analytical US
   As a:  Creator
 I want:  To see the engagement of each video through the number of likes
So That:  I can know which content attracts the more people. 
'''

SHOW_CMD = True


def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))

def print_rows(rows):
    table = PrettyTable()
    table.field_names = ["Video ID", "Hashtag", "Creator ID", "Creator Name", "Like Count"]
    for row in rows:
        table.add_row(row)
    print(table)

def get_video_engagement(creator_id):
    print("This function tracks and displays the engagement of videos created by a specific creator, "
          "measured by the number of likes each video has received.")

    tmpl = '''
    SELECT V.video_id, V.hashtag, C.creator_id, U.user_name AS creator_name,
           COUNT(L.like_id) AS like_count
      FROM "Like" L
      JOIN Videos V ON V.video_id = L.video_id
      JOIN Creator C ON V.creator_id = C.creator_id
      JOIN Users U ON C.creator_id = U.user_id
     WHERE C.creator_id = %s
     GROUP BY V.video_id, V.hashtag, C.creator_id, U.user_name
     ORDER BY like_count DESC;
    '''
    cur = conn.cursor()
    cur.execute(tmpl, (creator_id,))
    rows = cur.fetchall()
    print_rows(rows)
    cur.close()

if __name__ == '__main__':
    try:
        db, user = 'project', 'isdb'

        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True

        print(us)
        get_video_engagement(6)
        conn.close()
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))
