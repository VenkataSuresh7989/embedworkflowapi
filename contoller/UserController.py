from view import UserView

# ------------------------------------------- LOGIN --------------------------------------------------------------------
def is_login(form_data):
    return UserView.is_login(form_data)

# ------------------------------------------- CREATE USER --------------------------------------------------------------
def createuser(data, current_user, upload_image):
    return UserView.createuser(data, current_user, upload_image)

# ------------------------------------------- GET ALL USER INFO --------------------------------------------------------
def getallusers():
    return UserView.getallusers()

# ------------------------------------------- GET ALL EMPLOYEE DATA --------------------------------------------------------------
def getemptalldata():
    return UserView.getemptalldata()
# ------------------------------------------- UPDATE USER --------------------------------------------------------------
def update_user(emp_id, data, update_image):
    return UserView.update_user(emp_id, data, update_image)

# ------------------------------------------- DELETE USER --------------------------------------------------------------
def delete_user(idx):
    return UserView.delete_user(idx)
