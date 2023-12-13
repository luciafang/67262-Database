import psycopg2
from prettytable import PrettyTable

def heading(title):
    print('-' * 60)
    print("** %s:" % title)
    print('-' * 60, '\n')

heading("User Story #10 Track Likes per Hashtag")
print("Testing for Advertiser ID: 11")

SHOW_CMD = True
us = '''
* Complex (new)
  As an: Advertiser
I want: To easily track the number of likes my ads receive per hashtag
So That: I can quickly identify which hashtags are most effective in engaging my audience.
'''

def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))

def print_rows(rows):
    table = PrettyTable()
    table.field_names = ["Advertisor_id", "Hashtag", "Like Count"]
    for row in rows:
        table.add_row(row)
    print(table)

def track_likes_per_hashtag(advertiser_id):
    print("This function tracks and displays the number of likes ads receive per hashtag for a specific advertiser.")

    tmpl = '''
        SELECT v.advertiser_id, v.hashtag, COUNT(l.like_id) AS like_count
          FROM Videos AS v
          JOIN "Like" AS l ON v.video_id = l.video_id
         WHERE v.advertiser_id = %s AND v.is_advertisement = TRUE
         GROUP BY v.hashtag, v.advertiser_id
    '''

    cur = conn.cursor()
    cur.execute(tmpl, (advertiser_id,))
    rows = cur.fetchall()
    print_rows(rows)



if __name__ == '__main__':
    try:
        db, user = 'project', 'isdb'
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True
        cur = conn.cursor()

        print(us)
        track_likes_per_hashtag(11)
        conn.close()
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))
    except Exception as e:
        print("An error occurred: %s" % (e,))
