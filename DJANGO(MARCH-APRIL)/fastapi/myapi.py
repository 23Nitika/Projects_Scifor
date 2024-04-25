from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()
posts = []
post_id_counter = 0

class Post(BaseModel):
    id: int
    title: str
    content: str

@app.get("/posts/{post_id}", response_model=Post)
def get_post(post_id: int):
    try:
        return posts[post_id]
    except IndexError:
        raise HTTPException(status_code=404, detail="Post not found")

@app.get("/posts")
def get_all_posts():
    return posts

@app.post("/posts", response_model=Post)
def create_post(post: Post):
    post.id = len(posts)
    posts.append(post)
    return post


@app.put("/posts/{post_id}", response_model=Post)
def update_post(post_id: int, post: Post):
    try:
        posts[post_id] = post
        return post
    except IndexError:
        raise HTTPException(status_code = 404, detail="Post not found")


#delete
@app.delete("/posts/{post_id}")
def delete_post(post_id: int):
    try:
        del posts[post_id]
        return {"message": "Post deleted successfully"}
    except IndexError:
        raise HTTPException(status_code=404, detail="Post not found")

def fetch_data():
    import requests
    response = requests.get("http://127.0.0.1:8000/posts")
    if response.status_code == 200:
        return response.json()
    else:
        return None


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port = 8000)