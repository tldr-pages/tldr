# odps

> Aliyun ODPS (Open Data Processing Service) instrument de linie de comandă.
> Mai multe informaţii: <https://www.alibabacloud.com/help/doc-detail/27971.htm>

- Porniți linia de comandă cu un fișier de configurare personalizat:

`odpscmd --config={{odps_config.ini}}`

- Comutare proiect curent:

`use {{project_name}};`

- Afișați tabelele în proiectul curent:

`show tables;`

- Descrieți un tabel:

`desc {{table_name}};`

- Afișează partițiile de tabel:

`show partitions {{table_name}};`

- Descrieți o partiție:

`desc {{table_name}} partition ({{partition_spec}});`
