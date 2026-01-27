from view import TaskView

def getemptaskprogress(prod_id, emp_id):
    return TaskView.getemptaskprogress(prod_id, emp_id)

def getalltaskinfo(prod_idx):
    return TaskView.getalltaskinfo(prod_idx)

def gettaskinfo(emp_id, assign_by, prod_idx):
    return TaskView.gettaskinfo(emp_id, assign_by, prod_idx)


def gettaskbyidx(progress):
    return TaskView.gettaskbyidx(progress)


def gettaskbyemp_id(emp_id, progress):
    return TaskView.gettaskbyemp_id(emp_id, progress)


def createtask(prod_id, emp_id, data, img_arr):
    return TaskView.createtask(prod_id, emp_id, data, img_arr)


def updatetask(id, data, img_arr):
    return TaskView.updatetask(id, data, img_arr)


def delete_task(id):
    return TaskView.delete_task(id)


