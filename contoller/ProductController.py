from view import ProductView

def getallproducts():
    return ProductView.getallproducts()

def addproductsel(emp_id):
    return ProductView.addproductsel(emp_id)

def getproductsel(emp_id):
    return ProductView.getproductsel(emp_id)


def updateproductsel(emp_id, prod_sel):
    return ProductView.updateproductsel(emp_id, prod_sel)


def addproduct(data):
    return ProductView.addproduct(data)


def updateproductinfo(prod_sel, data):
    return ProductView.updateproductinfo(prod_sel, data)


def removeproduct(id):
    return ProductView.removeproduct(id)


