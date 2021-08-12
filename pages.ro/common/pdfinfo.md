# pdfinfo

> Vizualizator informaţii despre fişiere Portable Document Format (PDF).
> Mai multe informaţii: <https://www.xpdfreader.com/pdfinfo-man.html>

- Imprimare informații fișier PDF:

`pdfinfo {{path/to/file.pdf}}`

- Specificați parola de utilizator pentru fișierul PDF pentru a ocoli restricțiile de securitate:

`pdfinfo -upw {{password}} {{path/to/file.pdf}}`

- Specificați parola proprietarului pentru fișierul PDF pentru a ocoli restricțiile de securitate:

`pdfinfo -opw {{password}} {{path/to/file.pdf}}`
