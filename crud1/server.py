from fastapi import FastAPI
app=FastAPI()

'''
usage: Application Root Request
Rest API URL: http://localhost:8000/
Method Type: GET
Required Fields: None
Access Type: Public
'''
@app.get("/",description='This is Application Root Request')
def home_page():
    return {"message":"Home Page"}

'''
usage: Application About Request
Rest API URL: http://localhost:8000/about
Method Type: GET
Required Fields: None
Access Type: Public
'''
@app.get("/about",description="Application About Page")
def about_page():
    return {"message":"About Page"}