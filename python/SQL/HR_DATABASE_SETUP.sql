select * from employees;




 SELECT DISTINCT SALARY FROM EMPLOYEES A WHERE &N=(SELECT COUNT (DISTINCT B.SALARY)
 FROM EMPLOYEES B WHERE A.SALARY<=B.SALARY);

  SELECT DISTINCT SALARY FROM EMPLOYEES A;