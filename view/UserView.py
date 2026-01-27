import json
from datetime import timedelta, datetime
# from http.client import HTTPException
from fastapi import HTTPException, status
from config.database import connect_db, disconnect_db
from config.authentication import get_current_user, UserInDB, fake_hash_password, \
    ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, cipher_suite, getall_users, fake_users_info

# -------------------------------------------- LOGIN -------------------------------------------------------------------
from view.ProductView import addproductsel


def is_login(form_data):
    fake_users_db = []
    fake_users_db.extend(fake_users_info)
    fake_users_db.extend(getall_users())
    user_dict = get_current_user(fake_users_db, form_data.username)
    if not user_dict:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found."
        )

        # raise HTTPException()
    user = UserInDB(**user_dict)
    password = fake_hash_password(user.password)

    if not password == form_data.password:
        raise HTTPException(
            status_code=400,
            detail="Password mismatch."
        )

        # raise HTTPException()

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
    user.password = cipher_suite.decrypt(user.password).decode()
    return {"access_token": access_token, "token_type": "bearer", "user_info": user}

# -------------------------------------------- CREATE USER -------------------------------------------------------------

def createuser(data, current_user, upload_image):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        getInfo = json.loads(data)
        getInfo = getInfo[0]

        emp_id = json.loads(data)[0]['emp_id']

        if not check_emp_id(emp_id):
            return {"status": 400, "data": "User already exists."}
        else:
            getPwd =  cipher_suite.encrypt(getInfo['password'].encode())

            sql = "INSERT INTO `tbl_parent` (`id`, `emp_id`, `user_role`, `username`, `password`, `email`, `created_at`, `created_by`, `updated_at`, `updated_by`, `active_status`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            args = ("NULL", getInfo['emp_id'], getInfo['user_role'], getInfo['username'], getPwd, getInfo['email'],
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"), current_user.created_by, "", "", "0")

            cursor.execute(sql, args)
            conn.commit()

            user_photo = str(upload_image[0]) if (len(upload_image) > 0) else "" # getInfo['photo'] if 'photo' in getInfo else ""
            sql = "INSERT INTO `tbl_child` (`id`, `emp_id`, `job_role`, `qualification`, `skills`, `phoneno`, `address`, `photo`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            args = ("NULL", getInfo['emp_id'], getInfo['job_role'], getInfo['qualification'], getInfo['skills'],
                    getInfo['phoneno'], getInfo['address'], user_photo)

            cursor.execute(sql, args)
            conn.commit()

            resp = addproductsel(getInfo['emp_id'])
            if (resp['status'] == 200):
                fake_users_db = []
                fake_users_db.extend(fake_users_info)
                fake_users_db.extend(getall_users())
                return {"status": 200, "data": "New User added Successfully."}
            else:
                return {"status": 400, "data": resp.data}
    except Exception as e:
        print("Exception : ", e)
        return {"status": 500, "data": e}

def check_emp_id(emp_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        sql = "SELECT * FROM tbl_parent WHERE emp_id = %s"
        args = (emp_id)
        cursor.execute(sql, args)
        result = cursor.fetchone()
        if result:
            return False
        return True
    except Exception as e:
        print("Exception : ",e)
        return False

# --------------------------------------- GET ALL USER INFO ------------------------------------------------------------
def getallusers():
    return getall_users()

# --------------------------------------- GET ALL EMPLOYEE DATA ------------------------------------------------------------
def getemptalldata():
    try:
        conn = connect_db()
        cur = conn.cursor()
        query = "SELECT id, emp_id, username FROM tbl_user_info WHERE active_status = '0'"
        cur.execute(query)
        rows = cur.fetchall()
        return rows
    except Exception as e:
        print(e)
        return []

# --------------------------------------- UPDATE USER  -----------------------------------------------------------------

def update_user(emp_id, data, update_image):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        data = json.loads(data)[0]

        print(update_image)

        tbl_parent_keys = ["user_role", "username", "password", "email", "updated_by"]
        tbl_child_keys = ["job_role", "qualification", "skills", "phoneno", "address", "photo"]

        # Build update queries
        parent_sql = "UPDATE tbl_parent SET "
        parent_args = []
        child_sql = "UPDATE tbl_child SET "
        child_args = []

        if 'emp_id' in data:
            if update_emp_id(emp_id, data['emp_id']):
                emp_id = data['emp_id']
                data.pop('emp_id')
            else:
                return "Error"

        for item in data:
            if not (item in tbl_parent_keys or item in tbl_child_keys):
                print("item : ", item)
                return f"Invalid Key(s): {', '.join(item)}"

            if item in tbl_parent_keys:
                parent_sql += f"{item} = %s, "
                parent_args.append(data[item])
            elif item in tbl_child_keys:
                child_sql += f"{item} = %s, "
                child_args.append(data[item])

        if len(update_image) == 1:
            child_sql += f"photo = %s"
            child_args.append(update_image[0])

        # Add updated_at for parent table only
        parent_sql += f"updated_at = %s"
        parent_args.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        # Update both tables using emp_id
        parent_sql += f" WHERE emp_id = '{emp_id}'"
        child_sql += f" WHERE emp_id = '{emp_id}'"

        parent_sql = parent_sql.replace(',  WHERE', '  WHERE')
        child_sql = child_sql.replace(',  WHERE', '  WHERE')

        if "UPDATE tbl_parent SET  WHERE" not in parent_sql:
            cursor.execute(parent_sql, parent_args)
        if "UPDATE tbl_child SET  WHERE" not in child_sql:
            cursor.execute(child_sql, child_args)
        conn.commit()

        return {"status": 200, "data": "User details updated Successfully."}
    except Exception as e:
        return {"status": 500, "data": e}

def update_emp_id(old_emp_id, new_emp_id):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE tbl_parent SET emp_id = %s WHERE emp_id = %s", (new_emp_id, old_emp_id))
        cursor.execute("UPDATE tbl_child SET emp_id = %s WHERE emp_id = %s", (new_emp_id, old_emp_id))
        cursor.execute("UPDATE tbl_prod_idx SET emp_id = %s WHERE emp_id = %s", (new_emp_id, old_emp_id))
        cursor.execute("UPDATE tbl_task_info SET emp_id = %s WHERE emp_id = %s", (new_emp_id, old_emp_id))
        conn.commit()
        return True
    except Exception as e:
        return False

# --------------------------------------- DELETE USER  -----------------------------------------------------------------

def delete_user(idx):
    try:
        conn = connect_db()
        cur = conn.cursor()
        query = "UPDATE `tbl_parent` SET `active_status` = '1' WHERE `tbl_parent`.`emp_id` = %s;"
        args = [idx]
        result = cur.execute(query, args)
        disconnect_db(conn)
        if result > 0:
            return {"status": 200, "data": "User deleted Successfully."}
    except Exception as e:
        print(str(e))


