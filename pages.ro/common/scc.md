# scc

> Instrument scris în Go care contorizează liniile de cod.
> Mai multe informaţii: <https://github.com/boyter/scc>

- Tipăriți linii de cod în directorul curent:

`scc`

- Tipăriți linii de cod în directorul țintă:

`scc {{path/to/directory}}`

- Afișează ieșirea pentru fiecare fișier:

`scc --by-file`

- Afișează ieșirea folosind un format specific de ieșire (implicit la `tabular`):

`scc --format {{tabular|wide|json|csv|cloc-yaml|html|html-table}}`

- Numărați numai fișierele cu extensii de fișiere specifice:

`scc --include-ext {{go, java, js}}`

- Excludeți directoarele din a fi numărate:

`scc --exclude-dir {{.git,.hg}}`

- Afișează ieșirea și sortarea după coloană (implicit după fișiere):

`scc --sort {{files|name|lines|blanks|code|comments|complexity}}`

- Ajutor de imprimare pentru scc:

`scc -h`
