import psycopg2
from prettytable import PrettyTable

def heading(title):
    print('-' * 60)
    print(f"** {title}:")
    print('-' * 60, '\n')

heading("User Story #5: Fetch Whether is an advertisement")
print("Testing for Advertiser ID: 6")

us = '''
* Simple US
   As a:  Viewer
 I want:  To see whether the video is an advertisement
So That:  I can be more care to see whether I want to purchase the product or not. 
'''

SHOW_CMD = True

def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))

def print_rows(rows):
    table = PrettyTable()
    table.field_names = ["Video ID", "Duration (seconds)", "Upload Time", "Hashtag"]
    for row in rows:
        table.add_row(row)
    print(table)

def fetch_whether_is_advertisement(advertiser_id):
    print("This function fetches details of videos and checks if they are advertisements.")

    tmpl = '''
    SELECT video_id, duration, upload_time, hashtag
    FROM Videos
    WHERE is_advertisement = TRUE;
    '''

    cur = conn.cursor()
    cur.execute(tmpl, (advertiser_id,))
    rows = cur.fetchall()
    print_rows(rows)
    cur.close()

if __name__ == '__main__':
    try:
        db, user = 'project', 'isdb'
        conn = psycopg2.connect(database=db, user=user)
        conn.autocommit = True

        advertiser_id = 6 

        print(us)
        fetch_whether_is_advertisement(advertiser_id)
        conn.close()

    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))
