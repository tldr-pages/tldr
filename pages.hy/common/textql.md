# textql

> Կատարեք SQL-ը կառուցվածքային տեքստի դեմ, ինչպիսիք են CSV կամ TSV ֆայլերը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/dinedal/textql#usage>:.

- Տպեք նշված CSV ֆայլի տողերը, որոնք համապատասխանում են SQL հարցմանը `stdout`-ին:

`textql -sql "{{SELECT * FROM filename}}" {{path/to/filename.csv}}`

- Հարցրեք TSV ֆայլ.:

`textql -dlm=tab -sql "{{SELECT * FROM filename}}" {{path/to/filename.tsv}}`

- Հարցման ֆայլ վերնագրի տողով.:

`textql -dlm={{delimiter}} -header -sql "{{SELECT * FROM filename}}" {{path/to/filename.csv}}`

- Կարդացեք տվյալները `stdin`-ից՝:

`cat {{path/to/file}} | textql -sql "{{SELECT * FROM stdin}}"`

- Միացրեք երկու ֆայլ նշված ընդհանուր սյունակում.:

`textql -header -sql "SELECT * FROM {{path/to/file1}} JOIN {{file2}} ON {{path/to/file1}}.{{c1}} = {{file2}}.{{c1}} LIMIT {{10}}" -output-header {{path/to/file1.csv}} {{path/to/file2.csv}}`

- Ձևաչափեք ելքը՝ օգտագործելով ելքային սահմանազատիչ՝ ելքային վերնագրի տողով.:

`textql -output-dlm={{delimiter}} -output-header -sql "SELECT {{column}} AS {{alias}} FROM {{filename}}" {{path/to/filename.csv}}`
