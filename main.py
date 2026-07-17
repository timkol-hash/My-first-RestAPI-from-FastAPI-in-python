from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict

app = FastAPI()


class Post(BaseModel):
    post_id: int
    title: str
    body: str
    author_id: int


class Posts(BaseModel):
    posts: List[Post]


class User(BaseModel):
    id: int
    nick: str
    about: str
    posts: Posts


class Users(BaseModel):
    users: List[User]


users = Users(users=[
    User(id=1, nick="goodboy2000", about="i am a python devoloper", posts=Posts(posts=[
        Post(post_id=1, title="New Post", body="Very good post", author_id=1)
    ]))
])


@app.get('/posts/{post_id}')
async def getInfo(post_id: Optional[int] = None) -> Post:
    if post_id:
        for us in users.users:
            for post in us.posts.posts:
                if post.post_id == post_id:
                    return post
        raise HTTPException(status_code=404, detail="Post not found")
