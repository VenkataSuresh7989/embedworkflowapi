from view import BuildView

def getallbuildinfo(prod_idx):
    return BuildView.getallbuildinfo(prod_idx)

def getbuildinfo(type,option):
    return BuildView.getbuildinfo(type,option)


def createbuild(prod_id, data):
    return BuildView.createbuild(prod_id, data)


def updatebuild(emp_id, data):
    return BuildView.updatebuild(emp_id, data)


def delete_build(id):
    return BuildView.delete_build(id)


