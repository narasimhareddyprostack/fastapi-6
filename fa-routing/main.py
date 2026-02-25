from fastapi import FastAPI
from routes.user import router as userRouter
from routes.product import router as productRouter

app=FastAPI()

'''
usage: Application Root Request
REST API URL: http://127.0.0.1:8000/
Method Type:GET
Requrired Fields: None
Access Type:Public
'''
@app.get("/")
def root():
    return {"message":"Application Root Request"}

app.include_router(userRouter)
app.include_router(productRouter)