from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()


@app.get("/")
def root():
    return {"message": "welcome to my new api"}


@app.get('/posts')
def get_posts():
    return {'data': 'This is your post'}


@app.post('/createposts')
def create_posts(payLoad:):
    return {'message': 'successfully created'}