# pr

> Pagineer of kolomeer bestanden voor afdrukken.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/pr-invocation.html>.

- Toon meerdere bestanden met een standaardkop- en voettekst:

`pr {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Toon met een aangepaste gecentreerde koptekst:

`pr {{[-h|--header]}} "{{koptekst}}" {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Toon met genummerde regels en een aangepast datumnotatieformaat:

`pr {{[-n|--number-lines]}} {{[-D|--date-format]}} "{{formaat}}" {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Toon alle bestanden samen, één in elke kolom, zonder kop- of voettekst:

`pr {{[-m|--merge]}} {{[-T|--omit-pagination]}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Toon, beginnend bij pagina 2 en tot en met pagina 5, met een gegeven paginalengte (inclusief kop- en voettekst):

`pr +2:5 {{[-l|--length]}} {{paginalengte}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Toon met een offset voor elke regel en een afkappende aangepaste paginabreedte:

`pr {{[-o|--indent]}} {{offset}} {{[-W|--page_width]}} {{breedte}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`
