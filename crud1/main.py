from fastapi import FastAPI

#create FastAPI app
app=FastAPI()

'''
Usage: Application root request
API URL: http://localhost:8000/
Method Type:GET
Required Field:None
Access Type:Public
'''

@app.get("/")
def home_page():
    return {"message":"Welcome to FastAPI"}


'''
Usage: Application About request
API URL: http://localhost:8000/about
Method Type:GET
Required Field:None
Access Type:Public
'''
@app.get("/about")
def about_page():
    return {"message":"About Page"}

@app.get("/service")
def service_page():
    return {"message":"Service Page"}