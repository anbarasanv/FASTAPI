from os import stat
from typing import Optional
from fastapi import FastAPI, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
import psycopg2 as dbc
from psycopg2.extras import RealDictCursor
from pydantic.networks import HttpUrl
from starlette.responses import Response
import time
from .schema import Post

app = FastAPI()

while True:
    try:
        conn = dbc.connect(host='localhost', database='fastapi', user='postgres',
                        password='anba', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("DB Connected successfully!")
        break

    except Exception as err:
        print("Error while connecting to the DB:",err)
        time.sleep(2)


@app.get('/')
async def root():
    return {"message": "Hello World"}

@app.get('/posts')
async def get_posts(response: Response):
    cursor.execute("""SELECT * FROM posts;""")
    posts = cursor.fetchall()
    return {"posts": posts}

@app.get('/posts/{id}', status_code=status.HTTP_200_OK)
async def get_posts(id: int):
    cursor.execute(""" SELECT * FROM posts WHERE id = %s """, (str(id)))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,
                            detail=f"The post id: {id} did not found")
    return {"posts": post}

@app.post('/createposts', status_code=status.HTTP_201_CREATED)
async def create_posts(post: Post):
    cursor.execute("""INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",
                   (post.title, post.content, post.published))
    new_post = cursor.fetchone()
    conn.commit()
    return {"posts": new_post}

@app.delete('/deleteposts/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()

    if not deleted_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The requested id: {id} content not found")
    return {"posts": deleted_post}

@app.put('/posts/{id}', status_code=status.HTTP_200_OK)
async def update_post(id: int, post: Post):
    cursor.execute("UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *",
                   (post.title, post.content, post.published, str(id)))
    updated_post = cursor.fetchone()
    conn.commit()

    if not updated_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"updating id: {id} not found")
    return {"posts":updated_post}


