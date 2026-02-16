from fastapi import FastAPI

app=FastAPI()

#Application Root Request
@app.get("/",description='Application Root Request')
def root_requst():
    return {"message":"Root Request"}

'''
Rest API -1
--------------
usage: fetch all employees
Rest API URL: http://localhost:8000/employees
Method Type:GET
Required Fields:None 
Access Type:Public
'''
employees=[
    {"eid":101,"ename":"Rahul"},
    {"eid":102,"ename":"Sonia"},
    {"eid":103,"ename":"Priyanka"},
    {"eid":104,"ename":"Modi"},
]
@app.get("/employees")
def get_employees():
    return {"employees":employees,"Rest API":1}

'''
Rest API -2
--------------
usage: fetch employee by emp_id
Rest API URL: http://localhost:8000/employees/101
Method Type:GET
Required Fields:None 
Access Type:Public
'''
@app.get("/employees/{emp_id}")
def get_employee_details(emp_id:int):
    return {"Request Employee Id":emp_id,"Rest API":2}


'''
Rest API - 3
usage: fetch user by id and get orders
Rest API URL: http://localhost:8000/users/101/orders
Method Type:GET
Required Fields:None 
Access Type:Public

Note1:Path Parameter - identify the specific resouces
'''
@app.get("/users/{u_id}/orders")
def get_user_orders(u_id:int):
    return {"user Id":u_id,"Rest API":3}

""" 
Rest API - 4
usage: fetch user by id and get order detauls by order Id
Rest API URL: http://localhost:8000/users/101/orders/6
Method Type:GET
Required Fields:None 
Access Type:Public

Note1:Path Parameter - identify the specific resouces """

@app.get("/users/{u_id}/orders/{order_id}")
def get_user_order_details(u_id:int,order_id:int):
    return {"user Id":u_id,"Order Details":order_id,"Rest API":4}