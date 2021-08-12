# help2man

> Produceți pagini simple de om din ieșirea `—help 'și `—version` a executabilului.
> Mai multe informaţii: <https://www.gnu.org/software/help2man>

- Generează o pagină de om pentru un executabil:

`help2man {{executable}}`

- Specificați paragraful „nume” în pagina umană:

`help2man {{executable}} --name {{name}}`

- Specificați secțiunea pentru pagina de om (implicit la 1):

`help2man {{executable}} --section {{section}}`

- Ieșire la un fișier în loc de stdout:

`help2man {{executable}} --output {{path/to/file}}`

- Afișează ajutor detaliat:

`help2man --help`
