import psycopg2
from prettytable import PrettyTable

def heading(str):
    print('-' * 60)
    print("** %s:" % str)
    print('-' * 60, '\n')

heading("User Story #2: Calculate Total Money Earned")
print("Testing for Creator ID: 6")

us = '''
* Complex Analytical US
   As a:  Creator
 I want:  To see the total money earned by each video
So That:  I can understand which content is more profitable. 
'''

SHOW_CMD = True

def print_cmd(cmd):
    if SHOW_CMD:
        print(cmd.decode('utf-8'))

def print_rows(rows):
    table = PrettyTable()
    table.field_names = ["Creator ID", "Video ID", "Total Money Earned"]
    for row in rows:
        table.add_row(row)
    print(table)

def get_total_money_earned(creator_id):
    print("This function calculates and displays the total money earned by each video created by a specific creator.")

    tmpl = '''
    SELECT V.creator_id, V.video_id, SUM(M.amount) AS total_money
      FROM Videos V
      JOIN Money M ON V.video_id = M.video_id
     WHERE V.creator_id = %s
     GROUP BY V.video_id
     ORDER BY total_money DESC;
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
        get_total_money_earned(6)
        conn.close()
    except psycopg2.Error as e:
        print("Unable to open connection: %s" % (e,))
