python_db_con

이 파일은 DB2, Oracle, Postgre, sql server(MS SQL)을 연결하기 위해서 만든 통합 함수 입니다.

python_db_con의 python_db_connection을 import 하고

oracle의 경우, 설치 경로를 추가로 지정이 필요합니다. (나머지들은 안해줘도 됩니다)

DB연결 구분(oracle인지 oracle이 아닌지(db2, postgre, sql server)이 첫번째로 입력 되어야되고

(DB연결 구분이 4개 중 하나에 해당되지 않으면 확인을 요청하는 프린트가 나옵니다)

이후에는 HOST(IP), Port번호, Username, Password 순으로 되어있습니다.

Oracle은 추가로 앞에서 설정 해 놓은 설치 경로 객체를 추가로 넣으면 됩니다.

--------------------------------------------------------

1. 실제 수행 코드

from python_db_con import python_db_connection

oracle_install_space = 'oracle_설치 경로'

python_db_connection('oracle', 'DB명칭', 'host', 'port', 'id', 'pw',
                     oracle_install_space)

python_db_connection('db2', 'DB명칭', 'host', 'port', 'id', 'pw')

--------------------------------------------------------

2. 각 DB 개별 수행 코드

해당 py 내부 파일 개별 연결 함수들이 따로 존재합니다.

db2_con, oracle_con, sql_server_con, postgre_con으로 되어있습니다.

깃허브 블로그 중[python에서 Oracle, MS SQL, DB2, Postgre DB 연동 하는 법](https://bluemumin.github.io/python/2021/01/24/Python-python%EC%97%90%EC%84%9C-%EA%B0%81-DB-%EC%97%B0%EA%B2%B0%ED%95%98%EB%8A%94-%EB%B2%95/)

에 각 DB별 연결 방법 또한 적어 놓았습니다.

from python_db_con import 각 DBMS 개별 연결 함수를 사용하시거나

여러 DBMS 패키지까지 같이 import 되는걸 원하지 않으신다면, 따로 추출하셔서 사용하시는걸 권장드립니다.

--------------------------------------------------------

3. 동작 중 문제사항 발생시

해당 함수는 간단하게 구현한 것이고, 여러 DB를 매번 입력하는 것의 불편함을 해소하기 위해서

바로 여러 DBMS에 접속할 수 있도록 구현한 함수입니다.

imb_db_dbi, cx_Oracle, psycopg2, pymssql이 설치 되어있습니다.

각각 DB2, Oracle, postgre, sql server 연결용 패키지입니다.

만약 설치가 되지 않았다면 설치를 진행하여 주시기 바랍니다.

사용하지 않는 DBMS라면, .py파일에서 #로 해당 import와 해당 DBMS 함수, 

python_db_connection 안에 있는 if절 중 하나에 해당되는 DBMS를 제외 후 진행하여 주시기 바랍니다.
