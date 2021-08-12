# mlr

> Miller este ca `ciudat”, `sed`, `cut`, `join`, si `sort` pentru datele indexate cu nume, cum ar fi CSV, TSV si JSON tabelar.
> Mai multe informaţii: <https://johnkerl.org/miller/doc>

- Pretty-tipăriți un fișier CSV într-un format tabelar:

`mlr --icsv --opprint cat {{example.csv}}`

- Primiți datele JSON și imprimați destul de ieșire:

`echo '{"hello":"world"}' | mlr --ijson --opprint cat`

- Sortați alfabetic pe un câmp:

`mlr --icsv --opprint sort -f {{field}} {{example.csv}}`

- Sortare în ordine numerică descrescătoare pe un câmp:

`mlr --icsv --opprint sort -nr {{field}} {{example.csv}}`

- Conversia CSV la JSON, efectuarea calculelor și afișarea acestor calcule:

`mlr --icsv --ojson put '${{newField1}} = ${{oldFieldA}}/${{oldFieldB}}' {{example.csv}}`

- Primiți JSON și formatați ieșirea ca JSON vertical:

`echo '{"hello":"world", "foo":"bar"}' | mlr --ijson --ojson --jvstack cat`

- Filtrarea liniilor unui fișier CSV comprimat care tratează numerele ca șiruri de caractere:

`mlr --prepipe 'gunzip' --csv filter -S '${{fieldName}} =~ "{{regular_expression}}"' {{example.csv.gz}}`
