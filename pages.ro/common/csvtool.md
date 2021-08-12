# csvtool

> Utilitar pentru filtrarea și extragerea datelor din surse formatate CSV.
> Mai multe informaţii: <https://github.com/maroofi/csvtool>

- Extrageţi a doua coloană dintr-un fişier CSV:

`csvtool --column {{2}} {{path/to/file.csv}}`

- Extrageţi coloanele a doua şi a patra dintr-un fişier CSV:

`csvtool --column {{2,4}} {{path/to/file.csv}}`

- Extrageţi linii dintr-un fişier CSV în care coloana a doua se potriveşte exact cu „Foo”:

`csvtool --column {{2}} --search '{{^Foo$}}' {{path/to/file.csv}}`

- Extrageţi linii dintr-un fişier CSV în care a doua coloană începe cu 'Bar':

`csvtool --column {{2}} --search '{{^Bar}}' {{path/to/file.csv}}`

- Găsiți linii într-un fișier CSV în care a doua coloană se termină cu „Baz” și apoi extrageți coloanele a treia și a șasea:

`csvtool --column {{2}} --search '{{Baz$}}' {{path/to/file.csv}} | csvtool --no-header --column {{3,6}}`
