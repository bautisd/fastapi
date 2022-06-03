from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
#import . models
#import schemas
#from .routers import post
#from .routers import user
from .database import engine, get_db
#import auth
# import oauth2
#import config
#import vote

from . import models, schemas, oauth2
from .database import engine
from .routers import post, user, auth, vote
from .config import settings
from fastapi.middleware.cors import CORSMiddleware



# create the tables - using alembic to creata tables so dont need this
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()
# allow domains to talk to our api
origins = ['https://www.google.com']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)


my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1},
            {"title": "fav food", "content": "i klike pizza", "id": 2}
            ]


def find_post(id):
    for p in my_posts:
        if p['id'] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p['id'] == id:
            return i


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


# path operation or route
@app.get("/")
async def root():
    return {"message": "Hello World dave bdddd"}


# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
#    posts = db.query(models.Post).all()
#    return {"data":  posts}


# not working dont forget the update postman autherization
@app.get("/hello", response_model=List[schemas.Post])
def get_all_posts_from_user(db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)):
    # db: Session = Depends(get_db), current_user: int = Depends(oauth2.get_current_user)
    # RETURN ALL POSTS FROM CURRENT USER
    # using sql method
    # cursor.execute("""SELECT * FROM posts """)
    # posts = cursor.fetchall()
    print(current_user)
    # using orm sqlalchemy method
    posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()
    print(posts)
    return posts





