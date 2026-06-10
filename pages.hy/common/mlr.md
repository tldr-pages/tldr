# մլն

> Miller-ը նման է `awk`, `sed`, `cut`, `join` և `sort` տվյալների, օրինակ՝ CSV, TSV և աղյուսակային JSON:.
> Լրացուցիչ տեղեկություններ. <https://miller.readthedocs.io/en/latest/manpage/>:.

- Գեղեցիկ տպեք CSV ֆայլը աղյուսակային ձևաչափով.:

`mlr --icsv --opprint cat {{example.csv}}`

- Ստացեք JSON տվյալներ և գեղեցիկ տպեք արդյունքը.:

`{{echo '{"key":"value"}'}} | mlr --ijson --opprint cat`

- Դաշտի վրա դասավորել այբբենական կարգով.:

`mlr --icsv --opprint sort -f {{field}} {{example.csv}}`

- Դաշտի վրա դասավորել նվազման թվային կարգով.:

`mlr --icsv --opprint sort -nr {{field}} {{example.csv}}`

- Փոխակերպեք CSV-ն JSON-ի, կատարելով հաշվարկներ և ցուցադրեք այդ հաշվարկները.:

`mlr --icsv --ojson put '${{newField1}} = ${{oldFieldA}}/${{oldFieldB}}' {{example.csv}}`

- Ստացեք JSON և ձևաչափեք ելքը որպես ուղղահայաց JSON.:

`{{echo '{"key1":"value1", "key2":"value2"}'}} | mlr --ijson --ojson --jvstack cat`

- Զտեք սեղմված CSV ֆայլի տողերը, որոնք թվերը վերաբերվում են որպես [S] տողեր.:

`mlr --prepipe 'gunzip' {{[-c|--csv]}} filter {{[-S|--infer-none]}} '${{fieldName}} =~ "{{regex}}"' {{example.csv.gz}}`
