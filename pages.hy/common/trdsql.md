# trdsql

> Կատարեք SQL CSV, LTSV, JSON, YAML և TBLN ֆայլերի վրա:.
> Լրացուցիչ տեղեկություններ. <https://noborus.github.io/trdsql/>:.

- Փոխակերպեք օբյեկտի տվյալները բազմաթիվ JSON ֆայլերից CSV ֆայլի վերնագրով (`-oh`) և կրկնակի մեջբերումով.:

`trdsql -ocsv -oh "SELECT * FROM {{path/to/directory/*.json}}" | sed 's/\([^,]*\)/"&"/g' > {{path/to/file.csv}}`

- Մեկնաբանեք JSON ցուցակը որպես աղյուսակ և տեղադրեք առարկաները ներսում որպես սյունակներ (`path/to/file.json: {"list":[{"age":"26","name":"Tanaka"}]}`):

`trdsql "SELECT * FROM {{path/to/file.json}}::.list"`

- Շահագործել բարդ SQL հարցումը բազմաթիվ CSV ֆայլերի տվյալների հետ՝ առաջին տողով վերնագիր (`-ih`):

`trdsql -icsv -ih "SELECT {{column1,column2}} FROM {{path/to/file*.csv}} WHERE column2 != '' ORDER BY {{column1}} GROUP BY {{column1}}"`

- Միավորել 2 CSV ֆայլի բովանդակությունը մեկ CSV ֆայլի մեջ.:

`trdsql "SELECT {{column1,column2}} FROM {{path/to/file1.csv}} UNION SELECT {{column1,column2}} FROM {{path/to/file2.csv}}"`

- Միացեք PostgreSQL տվյալների բազային.:

`trdsql -driver postgres -dsn "host={{hostname}} port={{5433}} dbname={{database_name}}" "SELECT 1"`

- Ստեղծեք աղյուսակի տվյալները MySQL տվյալների բազայում CSV ֆայլից.:

`trdsql -driver mysql -dsn "{{username}}:{{password}}@{{hostname}}/{{database}}" -ih "CREATE TABLE {{table}} ({{column1}} int, {{column2}} varchar(20)) AS SELECT {{column3}} AS {{column1}},{{column2}} FROM {{path/to/header_file.csv}}"`

- Ցույց տալ տվյալները սեղմված տեղեկամատյան ֆայլերից.:

`trdsql -iltsv "SELECT * FROM {{path/to/access.log.gz}}"`
