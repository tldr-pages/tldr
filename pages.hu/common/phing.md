# phing

> Az Apache Anton alapuló PHP-építő eszköz. További információ: <https://www.phing.info>.

- Végezze el az alapértelmezett feladatot a `build.xml` fájlban:

`phing`

- Új build fájl inicializálása:

`phing -i {{path/to/build.xml}}`

- Egy adott feladat végrehajtása:

`phing {{task_name}}`

- Egyéni build fájl elérési útvonalának megadása:

`phing -f {{path/to/build.xml}} {{task_name}}`

- Naplófájl megadása a kimenethez:

`phing -b {{path/to/log_file}} {{task_name}}`

- Egyéni tulajdonságok megadása az építés során:

`phing -D{{property}}={{value}} {{task_name}}`

- Egyéni hallgató osztály megadása:

`phing -listener {{class_name}} {{task_name}}`

- Építés a verbózus kimenet használatával:

`phing -verbose {{task_name}}`
