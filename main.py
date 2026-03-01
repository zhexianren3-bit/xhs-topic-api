from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def root(): return {"msg": "小红书热门API"}
@app.get("/hot")
def hot():
    return {"success": True, "topics": [{"title": "热门1", "likes": 10000}]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
