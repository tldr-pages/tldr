# zgrep

> Grep tiparele de text din fișierele din fișierul comprimat (echivalent cu grep -Z).

- Grep un model într-un fișier comprimat (sensibil la majuscule):

`zgrep {{pattern}} {{path/to/compressed/file}}`

- Grep un model într-un fișier comprimat (insensibil la majuscule):

`zgrep -i {{pattern}} {{path/to/compressed/file}}`

- Numărul de linii de ieșire care conțin modelul potrivit într-un fișier comprimat:

`zgrep -c {{pattern}} {{path/to/compressed/file}}`

- Afișează liniile care nu au modelul prezent (Inversează funcția de căutare):

`zgrep -v {{pattern}} {{path/to/compressed/file}}`

- Grep un fișier comprimat pentru mai multe modele:

`zgrep -e "{{pattern_1}}" -e "{{pattern_2}}" {{path/to/compressed/file}}`

- Utilizați expresii regulate extinse (sprijin `? `, `+`,` {} `,` () `şi `|`):

`zgrep -E {{regular_expression}} {{path/to/file}}`

- Imprimați 3 linii de [C] ontext în jurul, [B] efore, sau [A] fter fiecare meci:

`zgrep -{{C|B|A}} {{3}} {{pattern}} {{path/to/compressed/file}}`
