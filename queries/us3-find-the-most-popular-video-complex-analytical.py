import psycopg2
from prettytable import PrettyTable

def heading(str):
    print('-' * 60)
    print("** %s:" % str)
    print('-' * 60, '\n')

heading("User Story #3: Find Most Popular Videos")
print("Identifying most popular videos based on likes.")

us = '''
* Complex & Analytical US 
   As a:  advertiser
 I want:  To see which video is the most popular based on the number of likes
So That:  I can make similar videos. 
'''

SHOW_CMD = True

def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))

def print_popular_video_rows(rows):
    table = PrettyTable()
    table.field_names = ["Video ID", "Hashtag", "Creator Name", "Like Count"]
    for row in rows:
        table.add_row(row)
    print(table)

def get_most_popular_videos():
    print("This function identifies the most popular videos based on the number of likes each video has received.")

    tmpl = '''
    SELECT V.video_id, V.hashtag, U.user_name AS creator_name, COUNT(L.like_id) AS like_count
      FROM Videos V
      JOIN "Like" L ON V.video_id = L.video_id
      JOIN Creator C ON V.creator_id = C.creator_id
      JOIN Users U ON C.creator_id = U.user_id
     GROUP BY V.video_id, V.hashtag, U.user_name
     ORDER BY like_count DESC;
    '''
    cur = conn.cursor()
    cur.execute(tmpl)
    rows = cur.fetchall()
    print_popular_video_rows(rows)
    cur.close()

if __name__ == '__main__':
    try:
        db, user = 'project', 'isdb'

        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True

        print(us)
        get_most_popular_videos()
        conn.close()
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))
    except Exception as e:
        print("An error occurred: %s" % (e,))
