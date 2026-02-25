from fastapi import APIRouter

router=APIRouter(prefix='/user')

@router.post('/create')
def create_user():
    return {"message":"New User Created Successfully"}

@router.get("/read")
def getusers():
    return {"message":"Getting all users"}

@router.get("/read/{uid}")
def get_user():
    return {"message":"Geting User Details by Id"}

@router.put("/update/{uid}")
def update_user():
    return {"message":"updating user by id"}

@router.delete("/delete/{uid}")
def delete_user():
    return {"message":"deleting user by id"}

