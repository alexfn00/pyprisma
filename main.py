from typing import Optional, Union

from fastapi import FastAPI
from prisma import Prisma
from pydantic import BaseModel

app = FastAPI()

class CreatePostData(BaseModel) :
    title: str
    content: Optional[str] = None
    published: bool
    

@app.get("/")
def list_posts():
    client = Prisma()
    client.connect()

    posts = client.post.find_many()

    client.disconnect()
    return posts

@app.post('/')
def create_post(dto: CreatePostData):
    
    try:
      client = Prisma()
      client.connect()
      print(dto)
      post = client.post.create(data=dto.model_dump(exclude_none=True))

      client.disconnect()
      return post
    except Exception as e:
          print(e)
    finally:
        print("aaa")