import json
from datetime import datetime

from config.common import table_verification
from config.database import connect_db, disconnect_db

"""
build_type		:	['Test','Release']  ['0','1']
build_option   	:	['Web','Mobile']    ['0','1']
"""

def getallbuildinfo(prod_idx):
    try:
        conn = connect_db()
        cur = conn.cursor()
        query = "SELECT * FROM tbl_build_info where `tbl_build_info`.`product_id` = %s AND `tbl_build_info`.`status` = '0' ORDER BY `build_date` DESC"
        cur.execute(query,[prod_idx])
        rows = cur.fetchall()
        return {"status": 200, "data": rows}
    except Exception as e:
        print(e)
        return []

def getbuildinfo(type,option):
    try:
        conn = connect_db()
        cur = conn.cursor()
        query = "SELECT * FROM tbl_build_info WHERE build_type = %s  OR build_option = %s AND status = '0' AND `tbl_build_info`.`status` = '0'"
        args = (type, option)
        cur.execute(query, args)
        rows = cur.fetchall()
        return {"status": 200, "data": rows}
    except Exception as e:
        print(e)
        return []


def createbuild(prod_id, data):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        getInfo = json.loads(data)
        getInfo = getInfo[0]
        # getInfo = getInfo #getInfo[0]

        # if table_verification('tbl_build_info', 'version', getInfo["version"]) == 0:
        sql = "INSERT INTO `tbl_build_info`(`id`, `product_id`, `build_date`, `build_name`, `build_type`, `build_path`, `build_option`, `fixed_list`, `version`, `created_by`,`build_status`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        args = ("NULL", prod_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), getInfo['build_name'], getInfo['build_type'], getInfo['build_path'], getInfo['build_option'], rf"{getInfo['fixed_list']}", getInfo['version'], getInfo['created_by'], '1')

        cursor.execute(sql, args)
        conn.commit()

        return {"status": 200, "data": "New build released Successfully."}
        # else:
        #     return {"status": 400, "data": "Version already exist."}
    except Exception as e:
        return {"status": 500, "data": e}

def updatebuild(id, data):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        data = json.loads(data)[0]

        build_sql = "UPDATE tbl_build_info SET "
        build_args = []

        for item in data:
            build_sql += f"{item} = %s, "
            build_args.append(data[item])

        build_sql += f"updated_at = %s"
        build_args.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        build_sql += f" WHERE `tbl_build_info`.`id` = '{id}'"
        build_sql = build_sql.replace(',  WHERE', '  WHERE')

        cursor.execute(build_sql, build_args)
        conn.commit()

        return {"status": 200, "data": "Build details updated Successfully."}
    except Exception as e:
        print("Exception : ", e)
        return {"status": 500, "data": e}

def delete_build(id):
    try:
        conn = connect_db()
        cur = conn.cursor()
        query = "UPDATE `tbl_build_info` SET `tbl_build_info`.`status` = '1' WHERE `id` = %s;"
        args = [id]
        result = cur.execute(query, args)
        disconnect_db(conn)
        if result > 0:
            return {"status": 200, "data": "Build deleted Successfully."}
    except Exception as e:
        print(str(e))


