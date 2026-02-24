from fastapi import FastAPI
from typing import Optional
app=FastAPI()

'''
Usage: Appliation Root Request
API URL: http://127.0.0.1:8000/
Method Type:GET
Required Fields: None
Access Type: Public
'''

@app.get("/")
def app_root():
    return {"message":"Application Root"}


'''
Usage: fk/google pixel req
API URL: http://127.0.0.1:8000/google-pixel?pid=p101&param=7788&ctx=c101&nnc=gp10&pageUID=2

API URL: http://127.0.0.1:8000/google-pixel?
pid=p101
&param=7788
&ctx=c101
&nnc=gp10
&pageUID=2

API URL: http://127.0.0.1:8000/google-pixel
API URL: http://127.0.0.1:8000/google-pixel?pid=101
API URL: http://127.0.0.1:8000/google-pixel?pid=101&param=7788
API URL: http://127.0.0.1:8000/google-pixel?pid=101&param=7788&ctx=c101
Method Type:GET
Required Fields: None
Access Type: Public
'''
@app.get("/google-pixel")
def get_producuts(pid:Optional[str]=None,param:Optional[str]=None,ctx:Optional[str]=None):
    return {"message":"Google Pixel","Product ID":pid,"param-Value":param,"CTX Value":ctx}


@app.post("/break")
def goto_breakfast():
    return {"message":"Today Breakfast is Idly"}