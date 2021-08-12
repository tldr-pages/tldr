# pdffonts

> Vizualizator de informaţii pentru fonturi portabile Document Format (PDF).
> Mai multe informaţii: <https://www.xpdfreader.com/pdffonts-man.html>

- Imprimați informații despre fonturile fișierelor PDF:

`pdffonts {{path/to/file.pdf}}`

- Specificați parola de utilizator pentru fișierul PDF pentru a ocoli restricțiile de securitate:

`pdffonts -upw {{password}} {{path/to/file.pdf}}`

- Specificați parola proprietarului pentru fișierul PDF pentru a ocoli restricțiile de securitate:

`pdffonts -opw {{password}} {{path/to/file.pdf}}`

- Imprimați informații suplimentare despre locația fontului care va fi utilizat atunci când fișierul PDF este rasterizat:

`pdffonts -loc {{path/to/file.pdf}}`

- Imprimați informații suplimentare despre locația fontului care va fi utilizat atunci când fișierul PDF este convertit în PostScript:

`pdffonts -locPS {{path/to/file.pdf}}`
