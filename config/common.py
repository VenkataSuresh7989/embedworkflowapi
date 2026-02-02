import json
import os
import uuid
# from http.client import HTTPException
from fastapi import HTTPException
from typing import List

from starlette import status
from config.authentication import oauth2_scheme, SECRET_KEY, ALGORITHM
from fastapi import Depends, UploadFile
from jose import jwt

import re

# ----------------------------------------- AUTH & TOKEN VERIFICATION --------------------------------------------------
from config.database import connect_db


def is_authorize(token):
    resp = auth_verification(token)
    if resp is not True:
        raise HTTPException(status_code=401, detail=resp)
    else:
        return resp

def auth_verification(token):
    if (user_authentication()):
        if (verifytoken(token) == True):
            return True
        else:
            return {"status": 401, "data": "Token has expired."}
    else:
        return {"status": 403, "data": "Authorized User."}


# ----------------------------------------- AUTHORIZATION --------------------------------------------------------------
def user_authentication(token: str = Depends(oauth2_scheme)):
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Not authorized. Please provide a valid token.",
                            headers={"WWW-Authenticate": "Bearer"}
                            )
    return True


# ----------------------------------------- TOKEN VERIFICATION ---------------------------------------------------------
def verifytoken(token: str):
    try:
        token_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        expiration_time = token_data["exp"]
        return True # {"status": 200, "data": f"Token expiration time: {expiration_time}"}
    except jwt.ExpiredSignatureError:
        return {"status": 400, "data": "Token has expired."}
    except jwt.JWTError:
        return {"status": 404, "data": "Token decoding failed."}


# ----------------------------------------- EMAIL VERIFICATION ---------------------------------------------------------
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# ----------------------------------------- DATA VERIFICATION in DB ----------------------------------------------------

def table_verification(tbl_name, tbl_label, item):
    try:
        conn = connect_db()
        cur = conn.cursor()
        query = "SELECT COUNT(*) FROM " + tbl_name + " WHERE " + tbl_label + " = %s"
        cur.execute(query,[item])
        rows = cur.fetchall()
        return rows[0]['COUNT(*)']
    except Exception as e:
        print(e)
        return {"status": 500, "data": []}

# ----------------------------------------- UPLOAD IMAGE ---------------------------------------------------------------

IMAGEDIR = "static/images/"

async def save_uploaded_files(path: str, files: List[UploadFile]) -> List[str]:
    getPath = IMAGEDIR + path
    saved_filenames = []

    if files.__len__() > 0:
        for file in files:
            unique_filename = f"{uuid.uuid4()}.jpg"  # Generate unique filename
            file_path = f"{getPath}{unique_filename}"

            try:
                contents = await file.read()  # Read file contents
                with open(file_path, "wb") as f:
                    f.write(contents)  # Save file to disk
                saved_filenames.append(unique_filename)
            except Exception as e:
                print(f"Error saving file {file.filename}: {e}")  # Log any errors

        return saved_filenames

def img_json_format(old_img_arr, img_arr):
    json_img = {}
    getLength = len(old_img_arr)

    if getLength > 0:
        json_img.update(old_img_arr)
    for i, item in enumerate(img_arr):
        idx = ((getLength) + i ) if (getLength > 0) else i
        json_img[f"img{idx + 1}"] = item
    return json.dumps(json_img)

def removeImages(imgArr,path):
    for img in imgArr:
        folder_path = IMAGEDIR + str(path) + imgArr[img]
        mage_path = f"{folder_path}"

        if os.path.exists(mage_path):
            os.remove(mage_path)
