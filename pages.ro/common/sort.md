# sort

> Sortarea liniilor de fișiere text.
> Mai multe informaţii: <https://www.gnu.org/software/coreutils/sort>

- Sortarea unui fișier în ordine crescătoare:

`sort {{path/to/file}}`

- Sortarea unui fișier în ordine descrescătoare:

`sort --reverse {{path/to/file}}`

- Sortați un fișier în mod insensibil la majuscule:

`sort --ignore-case {{path/to/file}}`

- Sortați un fișier folosind ordine numerică, mai degrabă decât alfabetică:

`sort --numeric-sort {{path/to/file}}`

- Sortează `/etc/passwd` după al treilea câmp al fiecărei linii numeric, folosind „:” ca separator de câmp:

`sort --field-separator={{:}} --key={{3n}} {{/etc/passwd}}`

- Sortarea unui fișier păstrând numai linii unice:

`sort --unique {{path/to/file}}`

- Sortați un fișier, tipăriți ieșirea în fișierul de ieșire specificat (poate fi folosit pentru a sorta un fișier în loc):

`sort --output={{path/to/file}} {{path/to/file}}`

- Sortează numerele cu exponenți:

`sort --general-numeric-sort {{path/to/file}}`
