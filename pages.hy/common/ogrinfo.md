#օգրինֆո

> Ցուցակել տեղեկատվություն OGR-ով աջակցվող տվյալների աղբյուրի մասին:.
> Լրացուցիչ տեղեկություններ. <https://gdal.org/en/stable/programs/ogrinfo.html>:.

- Ցուցակեք աջակցվող ձևաչափերը.:

`ogrinfo --formats`

- Թվարկեք տվյալների աղբյուրի շերտերը.:

`ogrinfo {{path/to/input.gpkg}}`

- Ստացեք մանրամասն տեղեկատվություն տվյալների աղբյուրի որոշակի շերտի մասին.:

`ogrinfo {{path/to/input.gpkg}} {{layer_name}}`

- Ցույց տալ տվյալների աղբյուրի որոշակի շերտի մասին ամփոփ տեղեկատվություն.:

`ogrinfo -so {{path/to/input.gpkg}} {{layer_name}}`

- Ցույց տալ տվյալների աղբյուրի բոլոր շերտերի ամփոփագիրը.:

`ogrinfo -so -al {{path/to/input.gpkg}}`

- Ցույց տալ պայմաններին համապատասխանող հատկանիշների մանրամասն տեղեկատվություն.:

`ogrinfo -where '{{attribute_name > 42}}' {{path/to/input.gpkg}} {{layer_name}}`

- Թարմացրեք շերտը տվյալների աղբյուրում SQL-ով.:

`ogrinfo {{path/to/input.geojson}} -dialect SQLite -sql "{{UPDATE input SET attribute_name = 'foo'}}"`
