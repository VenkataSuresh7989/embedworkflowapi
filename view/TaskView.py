import json
import os

from datetime import datetime
from config.common import table_verification, img_json_format, removeImages
from config.database import connect_db
from collections import defaultdict


def getemptaskprogress(prod_id, emp_id):
    try:
        conn = connect_db()
        cur = conn.cursor()

        query = "SELECT * FROM `tbl_task_info` WHERE `tbl_task_info`.`product_id` = %s AND `tbl_task_info`.`emp_id` = %s AND `tbl_task_info`.`status` = '0'"
        cur.execute(query, [prod_id, emp_id])
        rows = cur.fetchall()

        if(len(rows) > 0):
            employee_tasks = defaultdict(lambda: {"pending": 0, "inprogress": 0, "completed": 0})
            for task in rows:
                if emp_id == task["emp_id"]:
                    task_status = int(task["task_progress"])

                    if task_status == 0:
                        employee_tasks[emp_id]["pending"] += 1
                    elif task_status == 1:
                        employee_tasks[emp_id]["inprogress"] += 1
                    elif task_status == 2:
                        employee_tasks[emp_id]["completed"] += 1
            return {"status": 200, "data" : [employee_tasks[emp_id]['pending'], employee_tasks[emp_id]['inprogress'], employee_tasks[emp_id]['completed']]}
            # return [{"task_progress": task_count} for emp_id, task_count in employee_tasks.items()]
        return {"status": 200, "data" : rows}
    except Exception as e:
        print(e)
        return []


def getalltaskinfo(prod_idx):
    try:
        conn = connect_db()
        cur = conn.cursor()
        query = "SELECT * FROM tbl_task_info where `tbl_task_info`.`product_id` = %s AND `tbl_task_info`.`status` = '0' ORDER BY `assigned_at` DESC"
        cur.execute(query,[prod_idx])
        rows = cur.fetchall()
        for row_info in rows:
            row_info['emp_id'] = row_info['emp_id']
            print(row_info['emp_id'])
            if row_info['images'] != "":
                row_info['images'] = json.loads(row_info['images'])
        return rows
    except Exception as e:
        print(e)
        return []

def gettaskinfo(emp_id, assign_by,prod_idx):
    try:
        conn = connect_db()
        cur = conn.cursor()

        query = "SELECT * FROM `tbl_task_info` WHERE `tbl_task_info`.`product_id` = %s AND (`tbl_task_info`.`status` = '0' AND (emp_id = %s OR assigned_by = %s)) ORDER BY `assigned_at` DESC"
        cur.execute(query, (prod_idx, emp_id, assign_by))
        rows = cur.fetchall()

        if rows.__len__() > 0:
            for row_info in rows:
                row_info['images'] = json.loads(row_info['images'])
        return rows
    except Exception as e:
        print(e)
        return []


def gettaskbyidx(progress):
    try:
        conn = connect_db()
        cur = conn.cursor()
        query = "SELECT * FROM tbl_task_info WHERE task_progress = %s AND `tbl_task_info`.`status` = '0'"
        cur.execute(query, (progress))
        rows = cur.fetchall()
        rows[0]['images'] = json.loads(rows[0]['images'])
        return rows
    except Exception as e:
        print(e)
        return []


def gettaskbyemp_id(emp_id,progress):
    try:
        conn = connect_db()
        cur = conn.cursor()
        query = "SELECT * FROM tbl_task_info WHERE emp_id = %s AND task_progress = %s"
        cur.execute(query, (emp_id, progress))
        rows = cur.fetchall()
        rows[0]['images'] = json.loads(rows[0]['images'])
        return rows
    except Exception as e:
        print(e)
        return []

def createtask(prod_id, emp_id, data, img_arr):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        getInfo = json.loads(data)
        getInfo = getInfo[0]

        if table_verification('tbl_task_info', 'task', getInfo["version"]) == 0:
            if table_verification('tbl_task_info', 'task', getInfo["task"]) == 0:
                img_ingo = str(img_json_format({},img_arr)) if (len(img_arr) > 0) else "{}"

                sql = "INSERT INTO `tbl_task_info` (`id`, `product_id`, `emp_id`, `task`, `version`, `images`, `assigned_at`, `assigned_by`, `task_progress`, `status`)  VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                args = ("NULL", prod_id, emp_id, getInfo['task'], getInfo['version'] , img_ingo, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), getInfo['assigned_by'], '1', '0')

                cursor.execute(sql, args)
                conn.commit()
                return {"status": 200, "data": "New Task added Successfully."}
            else:
                return {"status": 400, "data": "Task already exist."}
        else:
            return {"status": 400, "data": "Version already exist."}
    except Exception as e:
        return {"status": 500, "data": e}


def updatetask(id, data, new_img_arr):
    try:
        conn = connect_db()
        cursor = conn.cursor()

        data = json.loads(data)[0]

        print("data : ", data)

        errMsg = ""
        resp = True

        if "version" in data and "task" in data:
            if not table_verification('tbl_task_info', 'task', data["version"]):
                resp = table_verification('tbl_task_info', 'task', data["task"]) == 0
            else:
                errMsg = "Version and Task already exist."
        elif "version" in data:
            resp = table_verification('tbl_task_info', 'task', data["version"]) == 0
            errMsg = "Version already exist." if not resp else ""
        elif "task" in data:
            resp = table_verification('tbl_task_info', 'task', data["task"]) == 0
            errMsg = "Task already exist." if not resp else ""

        if resp and not errMsg:
            build_args = []
            build_sql = "UPDATE `tbl_task_info` SET "

            # GET JSON converted Images data while sending old images and new images.
            getImgArr = img_json_format(data['images'] if "images" in data else {}, new_img_arr)
            build_args.append(getImgArr if getImgArr else "{}")
            build_sql += "`images` = %s, "

            for item in data:
                print("item : ", item)
                if item == "removed_images":
                    continue
                if item == "completed_at":
                    build_args.append(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                elif item != "images":
                    build_args.append(data[item])
                    build_sql += f"`{item}` = %s, "

            build_args.append(id)
            build_sql = build_sql.rstrip(', ') + " WHERE `tbl_task_info`.`id` = %s"

            resp = cursor.execute(build_sql, build_args)

            if ((resp > 0) and 'removed_images' in data):
                if (len(data['removed_images']) > 0) and (resp == 1):
                    imgArr = data['removed_images']
                    if (len(imgArr) > 0):
                        removeImages(imgArr, 'tasks/')

            conn.commit()
            return {"status": 200, "data": "Task updated Successfully."}
        else:
            return {"status": 400, "data": errMsg}
    except Exception as e:
        print("Exception : ", e)

        return {"status": 500, "data": str(e)}


def delete_task(id):
    try:
        conn = connect_db()
        cur = conn.cursor()

        query = "SELECT * FROM `tbl_task_info` WHERE `tbl_task_info`.`id` = %s"
        cur.execute(query, (id))
        getResp = cur.fetchall()

        query = "UPDATE `tbl_task_info` SET `tbl_task_info`.`status` = '1' WHERE `tbl_task_info`.`id` = %s"
        resp = cur.execute(query, (int(id)))

        imgArr = json.loads(getResp[0]['images'])
        if (resp == 1) and (len(imgArr) > 0):
            removeImages(imgArr, 'tasks/')

        conn.commit()
        return {"status": 200, "data": "Task deleted Successfully."}
    except Exception as e:
        print(str(e))


