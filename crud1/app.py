from fastapi import FastAPI
app=FastAPI()
#Appication Root Request
@app.get("/",description="Application root Req")
def home():
    return {"message":"Application Root Request"}
'''
usage:create new user
Rest API URL: http://127.0.0.1:8000/user/create
Method Type:POST
Required Feilds: uname,email,gender
Access Type:Public
'''
@app.post("/user/create")
def create_user():
    return {"message":"new user created successfully"}

'''
Rest API 2:
usage: get users
Rest API URL: http://127.0.0.1:8000/user/read
Method Type:GET
Required Fields:None
Access Type:Public
'''
users=[
    {'uid':101,'uname':'Rahul'},
    {'uid':102,'uname':'Sonia'},
    {'uid':103,'uname':'Priyanak'},
]

@app.get("/user/read", description="fetching user detials")
def get_users():
    return users

'''
RestAPI 3:
--------------
usage: update user by id      - PUT
Rest API URL: http://127.0.0.1:8000/user/101
Method Type:PUT
Required Fields:uname,email,gender
Access Type:Public
'''
@app.put("/user/{uid}")
def update_user():
    return {"message":"user updated successfully"}


'''
RestAPI 4:
--------------
usage: delete user by id      -
Rest API URL: http://127.0.0.1:8000/user/101
Method Type:DELETE
Required Fields:None
Access Type:Public
'''
@app.delete("/user/{uid}")
def delete_user():
    print("inside delete_user function")
    return {"message":"user deleted successfully"}