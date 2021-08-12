# mupdf

> Mf este un vizualizator ușor PDF, XPS și cărți electronice.
> Mai multe informaţii: <https://www.mupdf.com>

- Deschideţi un PDF pe prima pagină:

`mupdf {{filename}}`

- Deschideţi un PDF la pagina 3:

`mupdf {{filename}} {{3}}`

- Deschide o parolă securizată PDF:

`mupdf -p {{password}} {{filename}}`

- Deschideţi un PDF cu un nivel iniţial de zoom, specificat ca DPI, de 72:

`mupdf -r {{72}} {{filename}}`

- Deschideți un PDF cu culoare inversată:

`mupdf -I {{filename}}`

- Deschideți un PDF colorat roșu #FF0000 (sintaxa de culoare hexazecimală RRGGBB):

`mupdf -C {{FF0000}}`

- Deschideți un PDF fără anti-aliasing (0 = oprit, 8 = cel mai bun):

`mupdf -A {{0}}`
