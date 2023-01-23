# pdfinfo

> Portable Document Format (PDF) fájlinformációk megjelenítője. További információ: <https://www.xpdfreader.com/pdfinfo-man.html>.

- PDF-fájlinformációk nyomtatása:

`pdfinfo {{path/to/file.pdf}}`

- A biztonsági korlátozások megkerülése érdekében adja meg a PDF-fájl felhasználói jelszavát:

`pdfinfo -upw {{password}} {{path/to/file.pdf}}`

- Tulajdonos jelszó megadása a PDF-fájlhoz a biztonsági korlátozások megkerülése érdekében:

`pdfinfo -opw {{password}} {{path/to/file.pdf}}`
