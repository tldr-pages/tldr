# mongo

> MongoDB interaktív shell kliens. További információ: <https://docs.mongodb.com/manual/reference/program/mongo>.

- Csatlakozás egy adatbázishoz:

`mongo {{database}}`

- Csatlakozás egy adott állomáson, adott porton futó adatbázishoz:

`mongo --host {{host}} --port {{port}} {{database}}`

- Csatlakozás egy adott felhasználónévvel rendelkező adatbázishoz; a felhasználónak jelszót kell kérnie:

`mongo --username {{username}} {{database}} --password`

- Egy JavaScript kifejezés kiértékelése az adatbázisban:

`mongo --eval '{{JSON.stringify(db.foo.findOne())}}' {{database}}`
