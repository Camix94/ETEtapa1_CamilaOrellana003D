# ETEtapa1_CamilaOrellana003D

--USUARIO BASE DE DATOS DEL PROYECTO
CREATE USER ground_zero IDENTIFIED BY "1234";
GRANT CONNECT,RESOURCE TO ground_zero;
ALTER USER ground_zero DEFAULT TABLESPACE USERS QUOTA UNLIMITED ON USERS;

--EN CASO DE QUE SQL LE ARROJE UN ERROR AL INTENTAR CREAR EL USUARIO, EJECUTE LO SIGUIENTE:
alter session set "_ORACLE_SCRIPT"=true;

--ADMIN
Usuario: admin
Pass: duoc2021

--PATH
http://127.0.0.1:8000/
