# comm

> Selectați sau respingeți liniile comune pentru două fișiere. Ambele fișiere trebuie sortate.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/comm>

- Produce trei coloane separate de tab-uri: linii numai în primul fișier, linii numai în al doilea fișier și linii comune:

`comm {{file1}} {{file2}}`

- Tipăriți numai linii comune ambelor fișiere:

`comm -12 {{file1}} {{file2}}`

- Imprimați numai linii comune ambelor fișiere, citind un fișier din stdin:

`cat {{file1}} | comm -12 - {{file2}}`

- Obțineți linii găsite numai în primul fișier, salvând rezultatul într-un al treilea fișier:

`comm -23 {{file1}} {{file2}} > {{file1_only}}`

- Tipăriți linii găsite numai în al doilea fișier, atunci când fișierele nu sunt sortate:

`comm -13 <(sort {{file1}}) <(sort {{file2}})`
