import json
from config.database import connect_db, disconnect_db


def getallversioninfo():
    try:
        conn = connect_db()
        cur = conn.cursor()

        # Get module info
        cur.execute("SELECT * FROM tbl_module_info")
        module_rows = cur.fetchall()

        # Get firmware info
        cur.execute("SELECT * FROM tbl_fw_info")
        fw_rows = cur.fetchall()

        return {"status": 200, "data": {
            "tbl_module_info": module_rows,
            "tbl_fw_info": fw_rows
        }}

    except Exception as e:
        print("ERROR:", e)
        return {
            "tbl_module_info": [],
            "tbl_fw_info": []
        }

def createmodule(data):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        getInfo = json.loads(data)
        getInfo = getInfo[0]
        sql = "INSERT INTO `tbl_module_info`(`id`, `opti_server`, `cada`, `amp_android`, `amp_ios`, `msam`) VALUES (%s, %s, %s, %s, %s, %s)"
        args = ("NULL", getInfo['opti_server'], getInfo['cada'], getInfo['amp_android'], getInfo['amp_ios'], getInfo['msam'])

        cursor.execute(sql, args)
        conn.commit()

        return {"status": 200, "data": "New Module created."}
    except Exception as e:
        return {"status": 500, "data": e}


def updatemodule(id, data):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        data = json.loads(data)[0]

        build_sql = "UPDATE tbl_module_info SET "
        build_args = []

        for item in data:
            build_sql += f"{item} = %s, "
            build_args.append(data[item])

        build_sql += f" WHERE `tbl_module_info`.`id` = '{id}'"
        build_sql = build_sql.replace(',  WHERE', '  WHERE')

        cursor.execute(build_sql, build_args)
        conn.commit()

        return {"status": 200, "data": "Module details updated Successfully."}
    except Exception as e:
        print("Exception : ", e)
        return {"status": 500, "data": e}

def deletemodule(id):
    try:
        conn = connect_db()
        cur = conn.cursor()
        query = "DELETE FROM tbl_module_info WHERE id=%s"
        args = [id]
        cur.execute(query, args)
        conn.commit()
        return {"status": 200, "data": "Module deleted Successfully."}
    except Exception as e:
        print(str(e))


def createfw(data):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        getInfo = json.loads(data)
        getInfo = getInfo[0]
        sql = "INSERT INTO `tbl_fw_info`(`id`, `xpr`, `mb_ble`, `flex_max`) VALUES (%s, %s, %s, %s)"
        args = ("NULL", getInfo['xpr'], getInfo['mb_ble'], getInfo['flex_max'])

        cursor.execute(sql, args)
        conn.commit()

        return {"status": 200, "data": "New Firmware created."}
    except Exception as e:
        return {"status": 500, "data": e}


def updatefw(id, data):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        data = json.loads(data)[0]

        build_sql = "UPDATE tbl_fw_info SET "
        build_args = []

        for item in data:
            build_sql += f"{item} = %s, "
            build_args.append(data[item])

        build_sql += f" WHERE `tbl_fw_info`.`id` = '{id}'"
        build_sql = build_sql.replace(',  WHERE', '  WHERE')

        cursor.execute(build_sql, build_args)
        conn.commit()

        return {"status": 200, "data": "Firmware details updated Successfully."}
    except Exception as e:
        print("Exception : ", e)
        return {"status": 500, "data": e}

def deletefw(id):
    try:
        conn = connect_db()
        cur = conn.cursor()
        query = "DELETE FROM tbl_fw_info WHERE id=%s"
        args = [id]
        cur.execute(query, args)
        conn.commit()
        return {"status": 200, "data": "Firmware deleted Successfully."}
    except Exception as e:
        print(str(e))