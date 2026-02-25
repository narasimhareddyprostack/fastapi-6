from fastapi import APIRouter

router=APIRouter(prefix='/product')


@router.post("/create")
def create_product():
    return {"message":"New Product Created Successfully"}

@router.get("/read")
def get_all_products():
    return {"message":"Getting All Products"} 

@router.get("/read/{pid}")
def get_product():
    return {"message":"Getting Product Detials by Id"}

@router.put("/update/{pid}")
def update_product():
    return {"message":"Updating product by Id"}

@router.delete("/delete/{pid}")
def delete_product():
    return {"message":"deleting product by Id"}