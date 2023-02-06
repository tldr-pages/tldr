# dolt sql

> SQL-lekérdezés futtatása. Több SQL-kijelentést pontosvesszővel kell elválasztani. További információ: <https://docs.dolthub.com/cli-reference/cli#dolt-sql>.

- Egyetlen lekérdezés futtatása:

`dolt sql --query "{{INSERT INTO t values (1, 3);}}"`

- Az összes mentett lekérdezés listázása:

`dolt sql --list-saved`
