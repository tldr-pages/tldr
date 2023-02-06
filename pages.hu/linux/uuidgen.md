# uuidgen

> Egyedi azonosítók (UUID-k) generálása. Lásd még: `uuid`. További információ: <https://manned.org/uuidgen>.

- Hozzon létre egy véletlenszerű UUIDv4-et:

`uuidgen --random`

- UUIDv1 létrehozása az aktuális idő alapján:

`uuidgen --time`

- Létrehoz egy UUIDv5-öt a névből egy megadott névtér-előtaggal:

`uuidgen --sha1 --namespace {{@dns|@url|@oid|@x500}} --name {{object_name}}`
