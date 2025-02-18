select department_name, department_id from departments dep where exists
(
select * from EMPLOYEES emp where dep.DEPARTMENT_ID = emp.department_id
);