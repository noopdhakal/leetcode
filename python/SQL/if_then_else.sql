select decode(sex, "M", "Male", "F", "Female", 'Unknown') from Employees;

select decode(GREATEST(A, B), A, "A is greater than B", "B is greater than A") from dual;

select * from Employees;