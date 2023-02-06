# uuid

> Univerzálisan egyedi azonosítók (UUID) generálása és dekódolása. Lásd még: `uuidgen`. További információ: <https://manned.org/uuid>.

- UUIDv1 generálása (az idő és a rendszer hardvercíme alapján, ha van):

`uuid`

- UUIDv4 generálása (véletlenszerű adatok alapján):

`uuid -v {{4}}`

- Egyszerre több UUIDv4 azonosítót generál:

`uuid -v {{4}} -n {{number_of_uuids}}`

- UUIDv4 generálása és a kimeneti formátum megadása:

`uuid -v {{4}} -F {{BIN|STR|SIV}}`

- UUIDv4 generálása és a kimenet kiírása egy fájlba:

`uuid -v {{4}} -o {{path/to/file}}`

- UUIDv5 generálása (a megadott objektumnév alapján) egy megadott névtér-előtaggal:

`uuid -v {{5}} ns:{{DNS|URL|OID|X500}} {{object_name}}`

- Egy adott UUID dekódolása:

`uuid -d {{uuid}}`
