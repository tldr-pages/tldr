# pdffonts

> Portable Document Format (PDF) fájl betűtípusok információmegjelenítője. További információ: <https://www.xpdfreader.com/pdffonts-man.html>.

- PDF fájl betűtípusok információinak nyomtatása:

`pdffonts {{path/to/file.pdf}}`

- A biztonsági korlátozások megkerülése érdekében adja meg a PDF-fájl felhasználói jelszavát:

`pdffonts -upw {{password}} {{path/to/file.pdf}}`

- Tulajdonos jelszó megadása a PDF-fájlhoz a biztonsági korlátozások megkerülése érdekében:

`pdffonts -opw {{password}} {{path/to/file.pdf}}`

- A PDF-fájl raszterizálásakor használt betűtípus helyére vonatkozó további információk nyomtatása:

`pdffonts -loc {{path/to/file.pdf}}`

- A PDF-fájl PostScript-be történő átalakításakor használt betűtípus helyére vonatkozó további információk nyomtatása:

`pdffonts -locPS {{path/to/file.pdf}}`
