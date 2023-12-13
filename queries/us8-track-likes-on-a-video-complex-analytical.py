import psycopg2
from prettytable import PrettyTable

def heading(str):
    print('-' * 60)
    print("** %s:" % str)
    print('-' * 60, '\n')
    
heading("User Story #8 Track Likes on a specific video")
print("Testing for Video ID: 2")

us = '''
* Complex & Analytical US
   As a:  Creator
 I want:  I want to track my likes on a specific video 
So That:  I can evaluate my performance and see which video is popular.
'''
def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))


SHOW_CMD = True

def print_rows(rows):
    table = PrettyTable()
    table.field_names = ["Like Count"]
    for row in rows:
        table.add_row(row)
    print(table)

def fetch_like_count(video_id):
    print("This function tracks and displays the like of a specific video, "
          "measured by the number of likes each video has received.")
    
    tmpl = '''
    SELECT like_count as average_like_count
    FROM (
        SELECT COUNT(L.like_id) as like_count
          FROM "Like" L
          JOIN Videos V ON L.video_id = V.video_id
         WHERE V.video_id = %s
         GROUP BY V.video_id
    ) AS like_counts;
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
        fetch_like_count(2)
        conn.close()
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))
