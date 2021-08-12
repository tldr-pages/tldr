# jq

> Un procesor JSON linie de comandă care utilizează o limbă specifică domeniului.
> Mai multe informaţii: <https://stedolan.github.io/jq>

- Ieșiți un fișier JSON, în format destul de tipărit:

`jq . {{file.json}}`

- Ieșiți toate elementele din matrice (sau toate valorile din obiecte) într-un fișier JSON:

`jq '.[]' {{file.json}}`

- Citiți obiectele JSON dintr-un fișier într-o matrice și ieșiți-l (invers de `jq. [] `):

`jq --slurp . {{file.json}}`

- Ieșiți primul element dintr-un fișier JSON:

`jq '.[0]' {{file.json}}`

- Ieșiți valoarea unei chei date a fiecărui element într-un text JSON din stdin:

`cat {{file.json}} | jq 'map(.{{key_name}})'`

- Ieșiți valoarea mai multor chei ca obiect JSON nou (presupunând că intrarea JSON are cheile `key_name` și `other_key_name`):

`cat {{file.json}} | jq '{{{my_new_key}}: .{{key_name}}, {{my_other_key}}: .{{other_key_name}}}'`

- Combinați mai multe filtre:

`cat {{file.json}} | jq 'unique | sort | reverse'`

- Ieșiți valoarea unei chei date la un șir (și dezactivați ieșirea JSON):

`cat {{file.json}} | jq --raw-output '"some text: \(.{{key_name}})"'`
