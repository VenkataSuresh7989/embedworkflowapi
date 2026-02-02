import base64

from typing import Annotated
from pydantic import BaseModel
from jose import jwt, JWTError
from cryptography.fernet import Fernet
from datetime import timedelta, datetime
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status


#------------------------------------- Secret Key with Expired time ----------------------------------------------------
from config.database import connect_db

SECRET_KEY = "mendavenkatasuresh"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1440

secret_key = b'mendavenkatasuresh'
while len(secret_key) < 32:
    secret_key += secret_key

secret_key = secret_key[:32]
cipher_suite = Fernet(base64.urlsafe_b64encode(secret_key))

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

#------------------------------------- AUTHORIZATION TOKEN -------------------------------------------------------------
# GET USER DATA FROM DEFAULT INFO

# fake_users_db = [
#   {
#     "id": 1,
#     "emp_id": "EMBED7989",
#     "user_role": "3",
#     "username": "suresh",
#     "password": "gAAAAABk_Iw8WGlYGen1U5sflD2AiiJ0VMTdFNcIm2GroOrLK9a7F-0fHqlI0KYQhrBQ43Tf4-VWyJbC1PmY-9cK2RDYjUUdDg==",
#     "email": "suresh@gmail.com",
#     "created_at": "2023-12-01 15:12:57",
#     "created_by": "Nagesh",
#     "updated_at": "2023-12-01 15:16:11",
#     "updated_by": "Suresh",
#     "active_status": "0",
#     "job_role": "2",
#     "qualification": "B.Tech",
#     "skills": "JAVA,React,Vue,FastAPI",
#     "phoneno": "7989586850",
#     "address": "jhjsfh  jjshdjsad asddwdw jsbdjew sajdnweue jasdasdj jdajskdw ",
#     "photo": "7c50de12-d839-4e2d-97d8-9eb917b6e9d4.jpg",
#     "query": "Changes in Health Status, downstream and upstream configurations",
#     "assigned_by": "Nagesh",
#     "task_progress": "0"
#   },
#   {
#     "id": 2,
#     "emp_id": "EMBED7152",
#     "user_role": "1",
#     "username": "venkat",
#     "password": "gAAAAABlbWbyclXJgzpv_5uvTcwKQTx0Pm1x4HE5ZMKVeor5fpYAlOwahxR4va73jVrpRmqY89FKqAmBjVEtMzOe5Rc7DZjuWg==",
#     "email": "venkat@gmail.com",
#     "created_at": "2023-12-01 15:12:57",
#     "created_by": "Venkat",
#     "updated_at": "2023-12-01 15:16:11",
#     "updated_by": "Venkat",
#     "active_status": "0",
#     "job_role": "2",
#     "qualification": "BSC Compiuter",
#     "skills": "JAVA",
#     "phoneno": "159378620",
#     "address": "jfsdjfbsjs",
#     "photo": "",
#     "query": "",
#     "assigned_by": "suresh",
#     "task_progress": "0"
#   },
#   {
#     "id": 3,
#     "emp_id": "EMBED7859",
#     "user_role": "2",
#     "username": "sai",
#     "password": "gAAAAABlbWcWbc5eOZQptDizFq3loyTy7cA7-hMj-pC-eoVsT-LVMqvsA7EP3e4A7wvHiNX3kVX3p6Pyutf7K4Ud3muhiUY8bQ==",
#     "email": "sai@gmail.com",
#     "created_at": "2023-12-01 15:12:57",
#     "created_by": "Nagesh",
#     "updated_at": "2023-12-01 15:16:11",
#     "updated_by": "Sai",
#     "active_status": "0",
#     "job_role": "2",
#     "qualification": "Degree",
#     "skills": "",
#     "phoneno": "",
#     "address": "",
#     "photo": "7895641230",
#     "query": "dsjkfbdsjfbdsj bds",
#     "assigned_by": "Nagesh",
#     "task_progress": "0"
#   }
# ]
#
# def getall_users():
#     return fake_users_db
#
# if not fake_users_db:
#     fake_users_db = getall_users()

#---------------------------------------- GET Dynamic Database Data ----------------------------------------------------

# GET USER DATA FROM DATABASE
fake_users_db = []


fake_users_info =[
    {
        "id": 1,
        "emp_id": "EMBED0000",
        "user_role": "1",
        "username": "demo",
        "password": "gAAAAABlgvlruDROCfQ8I4DIbUMMC_vb8tJBpUpJWoN0GjRC6Dj8pwOureuJgpJmj-2G-wcT1P-EiMsapqbQHtNnK2b0_zm8mw==",
        "email": "demo@gmail.com",
        "created_at": "2023-12-01 15:12:57",
        "created_by": "demo",
        "updated_at": "2023-12-01 15:16:11",
        "updated_by": "demo",
        "active_status": "0",
        "job_role": "2",
        "qualification": "",
        "skills": "",
        "phoneno": "0123456789",
        "address": "",
        "photo": "7c50de12-d839-4e2d-97d8-9eb917b6e9d4.jpg",
        "query": "",
        "assigned_by": "demo",
        "task_progress": "0"
    }
]

def getall_users():
    try:
        conn = connect_db()
        cur = conn.cursor()
        # query = "select * from tbl_user_info WHERE active_status = '0'"
        query = "SELECT * FROM tbl_user_info WHERE active_status = '0' ORDER BY `tbl_user_info`.`emp_id` ASC"
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    except Exception as e:
        print(e)
        return []


# if not fake_users_db:
#    fake_users_db = getall_users()
fake_users_db.extend(fake_users_info)

if len(fake_users_db) == 1:
    fake_users_db.extend(getall_users())

# ---------------------------------------- Bearer Token ----------------------------------------------------------------
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
    id: int
    emp_id: str
    user_role: str
    username: str
    password: str
    email: str
    created_at: str
    created_by: str
    updated_at: str
    updated_by: str
    active_status: str
    job_role: str
    qualification: str
    skills: str
    phoneno: str
    address: str
    photo: str

class UserInDB(User):
    password: str

class TokenData(BaseModel):
    username: str

# ---------------------------------------- Decoding the login user password --------------------------------------------
def fake_hash_password(password: str):
    return cipher_suite.decrypt(password).decode()

# ---------------------------------------- Filter the login user details from database ---------------------------------
def get_user(db, username: str):
    for user_dict in db:
        if user_dict["username"] == username or user_dict["email"] == username:
            return UserInDB(**user_dict)

# ---------------------------------------- Getting login user details --------------------------------------------------
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail="Session expired.", headers={"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

# -------------------------- Getting login user detais from coockies based on login auth token -------------------------
async def get_current_active_user(current_user: Annotated[User, Depends(get_current_user)]):
    if current_user:
        return current_user
    else:
        raise HTTPException(status_code=400, detail="Inactive user")

# ---------------------------- Checking login username exist in database or not ----------------------------------------
def get_current_user(db,username):
    for user in db:
        if user["username"] == username:
            return user

# ---------------------------------------- Generating JWT Token based on login user details ----------------------------
def create_access_token(data: dict, expires_delta: timedelta ):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
