# pr

> Paginează sau coloanează fișiere pentru imprimare.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/pr>

- Imprimați mai multe fișiere cu un antet și subsol implicit:

`pr {{file1}} {{file2}} {{file3}}`

- Imprimați cu un antet centrat personalizat:

`pr -h "{{header}}" {{file1}} {{file2}} {{file3}}`

- Imprimare cu linii numerotate și un format de dată particularizat:

`pr -n -D "{{format}}" {{file1}} {{file2}} {{file3}}`

- Imprimați toate fișierele împreună, câte unul în fiecare coloană, fără antet sau subsol:

`pr -m -T {{file1}} {{file2}} {{file3}}`

- Imprimare, începând de la pagina 2 până la pagina 5, cu o lungime de pagină dată (inclusiv antet și subsol):

`pr +{{2}}:{{5}} -l {{page_length}} {{file1}} {{file2}} {{file3}}`

- Imprimați cu un decalaj pentru fiecare linie și o lățime de pagină particularizată trunchiere:

`pr -o {{offset}} -W {{width}} {{file1}} {{file2}} {{file3}}`
