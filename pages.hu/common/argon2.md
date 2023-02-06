# argon2

> Argon2 kriptográfiai hash-ok kiszámítása. További információ: <https://github.com/P-H-C/phc-winner-argon2#command-line-utility>.

- Számítson ki egy hash-t egy jelszóval és egy sóval az alapértelmezett paraméterekkel:

`echo "{{password}}" | argon2 "{{salt_text}}"`

- Hash kiszámítása a megadott algoritmussal:

`echo "{{password}}" | argon2 "{{salt_text}}" -{{d|i|id}}`

- A kimeneti hash megjelenítése további információk nélkül:

`echo "{{password}}" | argon2 "{{salt_text}}" -e`

- Hash kiszámítása megadott iterációs \[t\]imes, \[m\]emóriahasználat és \[p\]arallelitás paraméterekkel:

`echo "{{password}}" | argon2 "{{salt_text}}" -t {{5}} -m {{20}} -p {{7}}`
