#
# Database access functions for the web forum.
#

import time
import bleach
import psycopg2

## Database connection
DB = psycopg2.connect("dbname=forum")
cursor = DB.cursor()

## Get posts from database.
def GetAllPosts():
    '''Get all the posts from the database, sorted with the newest first.

    Returns:
      A list of dictionaries, where each dictionary has a 'content' key
      pointing to the post content, and 'time' key pointing to the time
      it was posted.
    '''
    cursor.execute("select time, content from posts order by time desc;")

    posts = ({'content': str(row[1]), 'time': str(row[0])} for row in cursor.fetchall())
    #posts = bleach.clean(posts)
    return posts
    '''
    posts = [{'content': str(row[1]), 'time': str(row[0])} for row in DB]
    posts.sort(key=lambda row: row['time'], reverse=True)
    return posts
    '''

## Add a post to the database.
def AddPost(content):
    '''Add a new post to the database.

    Args:
      content: The text content of the new post.
    '''
    content = bleach.clean(content)
    cursor.execute("insert into posts (content) values (%s) ", (content,))
    cursor.execute("delete from posts where content = 'cheese'")
    DB.commit()

    '''
    t = time.strftime('%c', time.localtime())
    DB.append((t, content))
    '''
    return
