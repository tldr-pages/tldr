# gcc

> Preprocesați și compilați fișierele sursă C și C++, apoi asamblați-le și legați-le împreună.
> Mai multe informaţii: <https://gcc.gnu.org>

- Compilați mai multe fișiere sursă în executabil:

`gcc {{source1.c}} {{source2.c}} --output {{executable}}`

- Permite avertismente, simboluri de depanare în ieșire:

`gcc {{source.c}} -Wall -Og --output {{executable}}`

- Includeți biblioteci dintr-o altă cale:

`gcc {{source.c}} --output {{executable}} -I{{header_path}} -L{{library_path}} -l{{library_name}}`

- Compilați codul sursă în instrucțiunile de asamblare:

`gcc -S {{source.c}}`

- Compilați codul sursă fără legătură:

`gcc -c {{source.c}}`
