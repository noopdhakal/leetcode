select decode(sex, "M", "Male", "F", "Female", 'Unknown') from Employees;

select decode(GREATEST(A, B), A, "A is greater than B", "B is greater than A") from dual;

select * from Employees;

Create table t2 as select <specific columns> from t1;
   Drop table t1;
   Rename t2 to t1;