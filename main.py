import uvicorn
import socket

from fastapi import FastAPI, File, UploadFile
from typing import Annotated, List
from datetime import datetime
from fastapi import Depends
from starlette.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordRequestForm





# -------------------------------------------- FAST API Instance -------------------------------------------------------
from config.authentication import cipher_suite, User, get_current_active_user
from config.common import save_uploaded_files
from contoller import UserController, BuildController, TaskController, VersionController, ProductController

app = FastAPI()

# ----------------------------------------- Enable Cross-Origin Resource Sharing (CORS) --------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------- Server Images Folders --------------------------------------------------------
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

# ------------------------------------------   IPAddress   -------------------------------------------------------------
@app.get("/getipaddress", tags=["IP Address"])
async def get_system_ip():
    hostname = socket.gethostname()  # System Name
    ip_address = socket.gethostbyname(hostname)
    return {"ipaddress": ip_address}

# ------------------------------------------   DATE & TIME   -----------------------------------------------------------

@app.get("/getdatetime", tags=["Date & Time"])
async def get_system_datetime():
    current_timestamp = datetime.now()
    return current_timestamp.strftime("%Y-%m-%d %H:%M:%S")

# -------------------------------------------- ENCODE & DECODE ---------------------------------------------------------
@app.get("/encode", tags=["ENCODE & DECODE"])
async def encode(password: str):
    return cipher_suite.encrypt(password.encode())


@app.get("/decode", tags=["ENCODE & DECODE"])
async def decode(password: str):
    return cipher_suite.decrypt(password).decode()

# ------------------------------------------ TESTING -------------------------------------------------------------------


# ------------------------------------------ USERS ---------------------------------------------------------------------

@app.get("/getalluser", tags=["USERS"])
def getparentallusers(current_user: Annotated[User, Depends(get_current_active_user)]):
    return UserController.getallusers()

@app.get("/getallempdata", tags=["USERS"])
def getemptalldata(current_user: Annotated[User, Depends(get_current_active_user)]):
    return UserController.getemptalldata()

@app.post("/token", tags=["USERS"])
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    return UserController.is_login(form_data)

@app.post("/register", tags=["USERS"])
async def read_users_me(data:str, current_user: Annotated[User, Depends(get_current_active_user)], files: List[UploadFile] = []):
    upload_image = await save_uploaded_files("users/", files)
    return UserController.createuser(data, current_user, upload_image)

@app.post("/updateuser", tags=["USERS"])
async def update_user(emp_id: str, data: str, current_user: Annotated[User, Depends(get_current_active_user)], files: List[UploadFile] = []):
    update_image = await save_uploaded_files("users/", files)
    img_arr = []
    if (update_image == None):
        img_arr = []
    elif len(update_image) > 0:
        img_arr = update_image
    return UserController.update_user(emp_id, data, img_arr)

@app.post("/deleteuser", tags=["USERS"])
async def delete_user(emp_id: str, current_user: Annotated[User, Depends(get_current_active_user)]):
    return UserController.delete_user(emp_id)

# ---------------------------------------------- PRODUCT INFO -------------------------------------------------------------
@app.get("/getallproducts", tags=["PRODUCTS"])
def getparentallusers(current_user: Annotated[User, Depends(get_current_active_user)]):
    return ProductController.getallproducts()

@app.get("/addproductsel", tags=["PRODUCTS"])
def addproductsel(emp_id: str,current_user: Annotated[User, Depends(get_current_active_user)]):
    return ProductController.addproductsel(emp_id)

@app.get("/getproductsel", tags=["PRODUCTS"])
def getproductsel(emp_id: str,current_user: Annotated[User, Depends(get_current_active_user)]):
    return ProductController.getproductsel(emp_id)

@app.post("/updateproductsel", tags=["PRODUCTS"])
async def updateproductsel(emp_id: str, prod_sel: str,  current_user: Annotated[User, Depends(get_current_active_user)]):
    return ProductController.updateproductsel(emp_id, prod_sel)

@app.post("/createproduct", tags=["PRODUCTS"])
async def addproduct(data:str,  current_user: Annotated[User, Depends(get_current_active_user)]):
    return ProductController.addproduct(data)


@app.post("/updateproductinfo", tags=["PRODUCTS"])
async def updateproductinfo(id: str, data: str, current_user: Annotated[User, Depends(get_current_active_user)]):
    return ProductController.updateproductinfo(id, data)

@app.post("/removeproduct", tags=["PRODUCTS"])
async def removeproduct(id: int, current_user: Annotated[User, Depends(get_current_active_user)]):
    return ProductController.removeproduct(id)

# ------------------------------------------ BUILD & RELEASE INFO ------------------------------------------------------

@app.get("/getallbuildinfo", tags=["BUILDS & RELEASE"])
def getallbuildinfo(prod_idx: str,current_user: Annotated[User, Depends(get_current_active_user)]):
    return BuildController.getallbuildinfo(prod_idx)

@app.get("/getbuildinfobyselection", tags=["BUILDS & RELEASE"])
def getparentallusers(type: str, option: str, current_user: Annotated[User, Depends(get_current_active_user)]):
    return BuildController.getbuildinfo(type,option)

@app.post("/createbuild", tags=["BUILDS & RELEASE"])
async def createbuild(prod_id: str, data:str, current_user: Annotated[User, Depends(get_current_active_user)]):
    return BuildController.createbuild(prod_id, data)

@app.post("/updatebuild", tags=["BUILDS & RELEASE"])
async def updatebuild(id: str, data: str, current_user: Annotated[User, Depends(get_current_active_user)]):
    return BuildController.updatebuild(id, data)

@app.post("/deletebuild", tags=["BUILDS & RELEASE"])
async def delete_build(id: str, current_user: Annotated[User, Depends(get_current_active_user)]):
    return BuildController.delete_build(id)

# ---------------------------------------------- TASK INFO -------------------------------------------------------------

@app.get("/getemptaskprogress", tags=["TASKS"])
def getemptaskprogress(prod_id,emp_id):
    return TaskController.getemptaskprogress(prod_id,emp_id)

@app.get("/getalltaskinfo", tags=["TASKS"])
async def getalltaskinfo(prod_idx: str, current_user: Annotated[User, Depends(get_current_active_user)]):
    return TaskController.getalltaskinfo(prod_idx)

@app.get("/gettaskinfo", tags=["TASKS"])
def gettaskinfo(emp_id: str, assign_by: str, prod_idx: int, current_user: Annotated[User, Depends(get_current_active_user)]):
    return TaskController.gettaskinfo(emp_id, assign_by, prod_idx)

@app.get("/gettaskbyidx", tags=["TASKS"])
def gettaskbyidx(progress: str, current_user: Annotated[User, Depends(get_current_active_user)]):
    return TaskController.gettaskbyidx(progress)

@app.get("/gettaskbyempidx", tags=["TASKS"])
def gettaskbyemp_id(emp_id: str, progress: str, current_user: Annotated[User, Depends(get_current_active_user)]):
    return TaskController.gettaskbyemp_id(emp_id, progress)

@app.post("/createtask", tags=["TASKS"])
async def createtask(prod_id: str, emp_id: str, data:str, current_user: Annotated[User, Depends(get_current_active_user)], files: List[UploadFile] = []): # files: List[UploadFile] = File(description="Multiple files as UploadFile")
    filenames = await save_uploaded_files("tasks/", files)
    img_arr = []
    if(filenames == None) :
        img_arr = []
    elif  len(filenames) >0:
        img_arr = filenames
    print("img_arr : ", img_arr)
    return TaskController.createtask(prod_id, emp_id, data, img_arr)

@app.post("/updatetask", tags=["TASKS"])
async def updatetask(id: str, data:str, current_user: Annotated[User, Depends(get_current_active_user)], files: List[UploadFile] = []):
    filenames = await save_uploaded_files("tasks/", files)
    img_arr = []
    if (filenames == None):
        img_arr = []
    elif len(filenames) > 0:
        img_arr = filenames
    return TaskController.updatetask(id, data, img_arr)

@app.post("/deletetask", tags=["TASKS"])
async def delete_task(id: str, current_user: Annotated[User, Depends(get_current_active_user)]):
    return TaskController.delete_task(id)

# ---------------------------------------------- VERSIONS INFO -------------------------------------------------------------

@app.get("/getversionsinfo", tags=["VERSIONS"])
async def getversionsinfo(current_user: Annotated[User, Depends(get_current_active_user)]):
    return VersionController.getallversioninfo()

@app.post("/createmodule", tags=["VERSIONS"])
async def createmodule(data:str, current_user: Annotated[User, Depends(get_current_active_user)]):
    return VersionController.createmodule(data)

@app.put("/updatemodule", tags=["VERSIONS"])
async def updatemodule(id:str, data:str, current_user: Annotated[User, Depends(get_current_active_user)]):
    return VersionController.updatemodule(id, data)

@app.post("/deletemodule", tags=["VERSIONS"])
async def deletemodule(id:str, current_user: Annotated[User, Depends(get_current_active_user)]):
    return VersionController.deletemodule(id)


@app.post("/createfw", tags=["VERSIONS"])
async def createfw(data:str, current_user: Annotated[User, Depends(get_current_active_user)]):
    return VersionController.createfw(data)

@app.put("/updatefw", tags=["VERSIONS"])
async def updatefw(id:str, data:str, current_user: Annotated[User, Depends(get_current_active_user)]):
    return VersionController.updatefw(id, data)

@app.post("/deletefw", tags=["VERSIONS"])
async def deletefw(id:str, current_user: Annotated[User, Depends(get_current_active_user)]):
    return VersionController.deletefw(id)


# -------------------------------------------- MAIN METHOD -------------------------------------------------------------
if __name__ == '__main__':
    # uvicorn.run(app)
    uvicorn.run(app, host="0.0.0.0", port=8000)
