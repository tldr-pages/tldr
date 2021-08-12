# fmt

> Reformatați un fișier text prin unirea paragrafelor sale și limitarea lățimii liniei la un anumit număr de caractere (75 în mod implicit).
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/fmt>

- Reformatarea unui fișier:

`fmt {{path/to/file}}`

- Reformatarea unui fișier care produce linii de ieșire de caractere (cel mult) `n`:

`fmt -w {{n}} {{path/to/file}}`

- Reformatați un fișier fără a uni linii mai scurte decât lățimea dată împreună:

`fmt -s {{path/to/file}}`

- Reformatarea unui fișier cu spațiere uniformă (1 spațiu între cuvinte și 2 spații între paragrafe):

`fmt -u {{path/to/file}}`
