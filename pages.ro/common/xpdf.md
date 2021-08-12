# xpdf

> Vizualizator de fişiere Portable Document Format (PDF).
> Mai multe informaţii: <https://www.xpdfreader.com/xpdf-man.html>

- Deschideţi un fişier PDF:

`xpdf {{path/to/file.pdf}}`

- Deschideți o anumită pagină într-un fișier PDF:

`xpdf {{path/to/file.pdf}} :{{page_number}}`

- Deschideţi un fişier PDF comprimat:

`xpdf {{path/to/file.pdf.tar}}`

- Deschideți un fișier PDF în modul ecran complet:

`xpdf -fullscreen {{path/to/file.pdf}}`

- Specificați zoom inițial:

`xpdf -z {{75}}% {{path/to/file.pdf}}`

- Specificați zoom inițial la lățimea paginii sau pagina completă:

`xpdf -z {{page|width}} {{path/to/file.pdf}}`
