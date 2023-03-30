from fastapi import FastAPI

app = FastAPI()

fake_blogs = [{"blog_name":"ABC"},{"blog_name":"blog blog"},{"blog_name":"Disney"}]

@app.get("/")
def index():
    return {"message":"hello world"}

@app.get("/blog/{id}")
def get_blog(id:int):
    return {"blog_id" : id}

"""
Path param : / 
Used to request like a single resource

Query Param : /?skip=1&limit=2
Used to request multiple resoures, filtering or sorting data
"""

@app.get("/blogs/")
def read_blog(skip:int=0,limit:int=1):
    return fake_blogs[skip:skip+limit]
