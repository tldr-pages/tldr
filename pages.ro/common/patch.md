# patch

> Corectează un fișier (sau fișiere) cu un fișier diff.
> Rețineți că fișierele diff ar trebui să fie generate de comanda `diff`.

- Aplicați un patch utilizând un fișier diff (numele fișierelor trebuie incluse în fișierul diff):

`patch < {{patch.diff}}`

- Aplicați un patch la un anumit fișier:

`patch {{path/to/file}} < {{patch.diff}}`

- Patch un fișier care scrie rezultatul într-un fișier diferit:

`patch {{path/to/input_file}} -o {{path/to/output_file}} < {{patch.diff}}`

- Aplicați un patch în directorul curent:

`patch -p1 < {{patch.diff}}`

- Aplicaţi reversul unui plasture:

`patch -R < {{patch.diff}}`
