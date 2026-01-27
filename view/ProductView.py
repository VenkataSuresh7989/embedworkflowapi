import json

from config.common import table_verification
from config.database import connect_db


def getallproducts():
    try:
        conn = connect_db()
        cur = conn.cursor()
        query = "SELECT * FROM tbl_products_info where `tbl_products_info`.`status` = '0'"
        cur.execute(query)
        rows = cur.fetchall()
        return {"status": 200, "data": rows}
    except Exception as e:
        print(e)
        return {"status": 500, "data": []}


def getproductsel(emp_id):
    try:
        conn = connect_db()
        cur = conn.cursor()
        query = "SELECT * FROM tbl_prod_idx where `tbl_prod_idx`.`emp_id` = %s"
        cur.execute(query,[emp_id])
        rows = cur.fetchall()
        return {"status": 200, "data": rows}
    except Exception as e:
        print(e)
        return {"status": 500, "data": []}


def addproductsel(emp_id):
    try:
        conn = connect_db()
        cur = conn.cursor()
        query = "INSERT INTO `tbl_prod_idx` (`id`, `emp_id`, `prod_idx`) VALUES (%s, %s, %s);"
        cur.execute(query, ('NULL', emp_id, '1'))
        conn.commit()
        return {"status": 200, "data": "New user Product Selcection created Successfully."}
    except Exception as e:
        print(e)
        return []

def updateproductsel(emp_id, prod_sel):
    try:
        conn = connect_db()
        cur = conn.cursor()
        query = "UPDATE `tbl_prod_idx` SET `prod_idx` = %s WHERE `tbl_prod_idx`.`emp_id` = %s;"
        cur.execute(query, (prod_sel, emp_id))
        conn.commit()
        return {"status": 200, "data": "Product Selcection updated Successfully."}
    except Exception as e:
        print(e)
        return []


def addproduct(data):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        getInfo = json.loads(data)
        getInfo = getInfo[0]

        if table_verification('tbl_products_info', 'name', getInfo["txtName"]) == 0:
            sql = "INSERT INTO `tbl_products_info` (`id`, `name`, `frontend`, `backend`, `database`, `framework`, `status`)  VALUES (%s, %s, %s, %s, %s, %s, %s)"
            args = ("NULL", getInfo["txtName"], getInfo["txtFrontend"], getInfo["txtBackend"] , getInfo["txtDatabase"], getInfo["txtFramework"], '0')

            cursor.execute(sql, args)
            conn.commit()
            return {"status": 200, "data": "New Product added Successfully."}
        else:
            return {"status": 400 , "data": "Product already exist."}
    except Exception as e:
        return {"status": 500, "data": e}


def updateproductinfo(prod_sel, data):
    try:
        conn = connect_db()
        cur = conn.cursor()

        data = json.loads(data)[0]
        errMsg = ""
        resp = True
        if "name" in data:
            resp = table_verification('tbl_products_info', 'name', data["name"]) == 0
            errMsg = "Product name is already exist." if not resp else ""

        if resp and not errMsg:
            build_args = []
            build_sql = "UPDATE `tbl_products_info` SET "

            for item in data:
                build_args.append(data[item])
                build_sql += f"`{item}` = %s, "

            build_args.append(int(prod_sel))
            build_sql = build_sql.rstrip(', ') + " WHERE `tbl_products_info`.`id` = %s"

            cur.execute(build_sql, build_args)
            conn.commit()

            return {"status": 200, "data": "Product updated Successfully."}
        else:
            return {"status": 400, "data": errMsg}
    except Exception as e:
        print(e)
        return []


def removeproduct(id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = "UPDATE `tbl_products_info` SET `status` = '1' WHERE `tbl_products_info`.`id` = %s"

        cursor.execute(sql, (id))
        conn.commit()
        return {"status": 200, "data": "Product removed Successfully."}

    except Exception as e:
        return {"status": 500, "data": e}


