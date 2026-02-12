from fastapi import FastAPI

#create FastAPI app
app=FastAPI()



@app.get("/")
def home_page():
    return {"message":"Welcome to FastAPI-app file"}


@app.get("/about")
def about_page():
    return {"message":"About Page -app file"}

@app.get("/service")
def service_page():
    return {"message":"Service Page -app file"}

@app.get("/contact")
def contact_page():
    return {"messge":"contact page - app file"}