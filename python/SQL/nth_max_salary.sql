select * from employees;

SELECT DISTINCT SALARY FROM employees A WHERE &N=(SELECT COUNT (DISTINCT B.SALARY)
 FROM employees B WHERE A.SALARY<=B.SALARY);

 SELECT DISTINCT SALARY FROM employees WHERE SALARY NOT IN
 (SELECT SALARY FROM employees WHERE SALARY < ANY (SELECT SALARY FROM employees));