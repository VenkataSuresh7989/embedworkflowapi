import json
from collections import defaultdict

from config.database import connect_db

def createtoolheaders(headername):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = "INSERT INTO `tbl_tool_headers`(`id`, `name`) VALUES (%s, %s)"
        args = ("NULL", headername)

        cursor.execute(sql, args)
        conn.commit()

        return {"status": 200, "data": "New header added Successfully."}
    except Exception as e:
        return {"status": 500, "data": e}

def updatetoolheaders(header_id, headername):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = "UPDATE `tbl_tool_headers` SET `name` = %s WHERE `id` = %s"
        args = (headername, header_id)

        resp = cursor.execute(sql, args)
        conn.commit()

        if resp > 0:
            return {"status": 200, "data": "Header updated successfully."}
        else:
            return {"status": 400, "data": "Header not found or no changes made."}

    except Exception as e:
        return {"status": 500, "data": str(e)}

def deletetoolheader(name):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = "DELETE FROM `tbl_tool_headers` WHERE `name` = %s"
        args = (name,)

        resp = cursor.execute(sql, args)
        conn.commit()

        if resp > 0:
            return { "status": 200, "data": "Header and related items deleted successfully." }
        else:
            return { "status": 400, "data": "Header not found." }

    except Exception as e:
        return {
            "status": 500,
            "data": str(e)
        }




def createtoolheaderItems(data):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        getInfo = json.loads(data)
        getInfo = getInfo[0]

        sql = "INSERT INTO `tbl_tool_header_items`(`id`, `header_id`, `label`, `value`, `is_copy`) VALUES (%s, %s, %s, %s, %s)"
        args = ("NULL", getInfo['header_id'], getInfo['label'], getInfo['value'], getInfo['is_copy'])

        cursor.execute(sql, args)
        conn.commit()

        return {"status": 200, "data": "New header items added Successfully."}
    except Exception as e:
        return {"status": 500, "data": e}

def updatetoolheaderItems(header_id, data):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        data = json.loads(data)[0]

        build_args = []
        build_sql = "UPDATE `tbl_tool_header_items` SET "

        for item in data:
            build_args.append(data[item])
            build_sql += f"`{item}` = %s, "

        build_args.append(header_id)
        build_sql = build_sql.rstrip(', ') + " WHERE `tbl_tool_header_items`.`id` = %s"

        resp = cursor.execute(build_sql, build_args)
        conn.commit()

        if resp > 0:
            return {"status": 200, "data": "Header items updated successfully."}
        else:
            return {"status": 400, "data": "Header items not found or no changes made."}

    except Exception as e:
        return {"status": 500, "data": str(e)}

def deletetoolheaderItems(id):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        sql = "DELETE FROM `tbl_tool_header_items` WHERE `id` = %s"
        args = (id)

        resp = cursor.execute(sql, args)
        conn.commit()

        if resp > 0:
            return { "status": 200, "data": "Header item and related items deleted successfully." }
        else:
            return { "status": 400, "data": "Header item not found." }

    except Exception as e:
        return { "status": 500, "data": str(e) }

def get_tool_headers_with_items():
    try:
        conn = connect_db()
        cur = conn.cursor()

        query = """SELECT h.id AS header_id, h.name AS header_name, i.id AS item_id, i.label, i.value, i.is_copy
            FROM tbl_tool_headers h LEFT JOIN tbl_tool_header_items i ON h.id = i.header_id ORDER BY h.id ASC"""

        cur.execute(query)
        rows = cur.fetchall()

        headers = defaultdict(lambda: {"id": None, "name": "", "items": []})

        for row in rows:
            hid = row["header_id"]

            if headers[hid]["id"] is None:
                headers[hid]["id"] = hid
                headers[hid]["name"] = row["header_name"]

            if row["item_id"] is not None:
                headers[hid]["items"].append({
                    "id": row["item_id"],
                    "label": row["label"],
                    "value": row["value"],
                    "is_copy": row["is_copy"]
                })

        return { "status": 200, "data": list(headers.values())}

    except Exception as e:
        print(e)
        return { "status": 500, "data": str(e) }