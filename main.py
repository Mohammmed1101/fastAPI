from fastapi import FastAPI

app = FastAPI()

@app.get("/posts")
def get_all_posts():
     
