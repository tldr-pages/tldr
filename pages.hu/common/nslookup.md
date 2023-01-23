# nslookup

> Névkiszolgáló(k) lekérdezése különböző domainrekordok számára. További információ: <https://manned.org/nslookup>.

- Kérdezze le a rendszer alapértelmezett névkiszolgálóját a tartomány IP-címéről (A rekord):

`nslookup {{example.com}}`

- Egy adott névkiszolgáló lekérdezése a tartomány NS rekordjához:

`nslookup -type=NS {{example.com}} {{8.8.8.8}}`

- Egy IP-cím fordított keresése (PTR rekord) lekérdezése:

`nslookup -type=PTR {{54.240.162.118}}`

- Bármely elérhető rekord lekérdezése TCP protokoll segítségével:

`nslookup -vc -type=ANY {{example.com}}`

- Egy adott névkiszolgáló lekérdezése a tartomány teljes zónafájljáról (zónatranszfer) TCP protokoll segítségével:

`nslookup -vc -type=AXFR {{example.com}} {{name_server}}`

- A tartomány levelezőszerverének lekérdezése (MX rekord), a tranzakció részleteinek megjelenítése:

`nslookup -type=MX -debug {{example.com}}`

- Egy adott névkiszolgáló lekérdezése egy adott portszámon a tartomány TXT rekordjára:

`nslookup -port={{port_number}} -type=TXT {{example.com}} {{name_server}}`
