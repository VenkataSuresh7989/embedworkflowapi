tbl_parent:
----------
	id		    	:	primarykey
	emp_id			:	
	user_role		:	['SuperAdmin','Admin','Manager','Employee']	['0','1','2','3']
	username		:	
	password		:	
	email			:
	created_at		:	
	created_by		:	
	updated_at		:	
	updated_by		:	
	active_status	:	['Active','Inactive']	['0','1']

tbl_child:
---------
	id			    :	primarykey
	emp_id			:	
	job_role		:	['SoftwareEngineer','FullStackDeveloper','FrontEndDeveloper','BackEndDeveloper','Tester','UI Designer'] ['0','1','2','3','4','5']
	qualification	:	
	skills			:	
	phoneno			:	
	address			:	
	photo			:	

tbl_task_info:	
-------------
	id			    :	primarykey
	emp_id			:	
	task			:	
	assigned_at		:	
	assigned_by		:	
	task_progress	:	['In Progress','Pending','Completed']	['0','1','2']
	status          :   ['0','1']

tbl_build_info:	
--------------	
	id			    :	primarykey
	build_date		:	
	build_type		:	['Test','Release']  ['0','1']
	build_option	:	['Web','Mobile']    ['0','1']
	fixed_list		:	
    build_path      :   
    build_status    :   ['In progress', 'Success', 'Failed']  ['0', '1', '2']
    remark          :     
	version			:   

tbl_prod_idx:	
--------------	
	id			    :	primarykey
	emp_id		    :	
	prod_idx		:	

************************************************************************************************************************
Merge 2 user_info in DB:
-----------------------
CREATE VIEW tbl_user_info AS
SELECT
  t1.id,
  t1.emp_id,
  t1.user_role,
  t1.username,
  t1.password,
  t1.email,
  t1.created_at,
  t1.created_by,
  t1.updated_at,
  t1.updated_by,
  t1.active_status,
  t2.job_role,
  t2.qualification,
  t2.skills,
  t2.phoneno,
  t2.address,
  t2.photo
FROM tbl_parent t1
JOIN tbl_child t2 ON t1.emp_id = t2.emp_id;

************************************************************************************************************************











