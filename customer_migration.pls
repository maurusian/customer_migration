--so console output would work
SET SERVEROUTPUT on;
/

DECLARE
  i NUMBER;
  p_id NUMBER;
  
  CURSOR c IS
    SELECT *
    FROM UPD_CUSTOMERS;
    
  CURSOR f(p_id NUMBER) IS
    SELECT ID, UPDATE_DATE, LOCATION
    FROM
    (
    SELECT ID, UPDATE_DATE, LOCATION
    FROM UPD_CUSTOMERS
    WHERE ID = p_id
    ORDER BY UPDATE_DATE desc
    )
    WHERE ROWNUM = 1;
    
    r c%ROWTYPE;
    u f%ROWTYPE;
BEGIN
  
  FOR r in c LOOP
     OPEN f(r.ID);
     FETCH f INTO u;
     
     IF r.UPDATE_DATE >= u.UPDATE_DATE THEN
       IF r.UPDATE_FLAG = 'U' THEN
           BEGIN
             UPDATE CUSTOMERS
             SET LOCATION = r.LOCATION, UPDATE_DATE = r.UPDATE_DATE
             WHERE ID = r.ID;
           EXCEPTION
           WHEN OTHERS THEN
             DBMS_OUTPUT.PUT_LINE('Update Error for CUSTOMER '||r.ID);
             DBMS_OUTPUT.PUT_LINE(SQLERRM);
           END;
       ELSIF r.UPDATE_FLAG = 'I' THEN
           BEGIN
             INSERT INTO CUSTOMERS VALUES(r.ID,r.UPDATE_DATE,r.LOCATION);
           EXCEPTION
           WHEN OTHERS THEN
             DBMS_OUTPUT.PUT_LINE('Insertion Error for CUSTOMER '||r.ID);
             DBMS_OUTPUT.PUT_LINE(SQLERRM);
           END;
       ELSIF r.UPDATE_FLAG = 'D' THEN
           BEGIN
             DELETE FROM CUSTOMERS 
             WHERE ID = r.ID;
           EXCEPTION
           WHEN OTHERS THEN
             DBMS_OUTPUT.PUT_LINE('Deletion Error for CUSTOMER '||r.ID);
             DBMS_OUTPUT.PUT_LINE(SQLERRM);
           END;
       END IF;
     END IF;
     CLOSE f;
  END LOOP;
  --CLOSE c;
  COMMIT;
END;
/