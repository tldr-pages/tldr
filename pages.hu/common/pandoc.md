# pandoc

> Dokumentumok konvertálása különböző formátumok között. További információ: <https://pandoc.org>.

- Fájl átalakítása PDF-be (a kimeneti formátumot a fájlkiterjesztés határozza meg):

`pandoc {{input.md}} -o {{output.pdf}}`

- Kényszeríti a konvertálást egy adott formátum használatára:

`pandoc {{input.docx}} --to {{gfm}} -o {{output.md}}`

- Konvertálás önálló fájlba a megfelelő fejlécekkel/láblécekkel (LaTeX, HTML stb. esetén):

`pandoc {{input.md}} -s -o {{output.tex}}`

- Az összes támogatott bemeneti formátum felsorolása:

`pandoc --list-input-formats`

- Az összes támogatott kimeneti formátum felsorolása:

`pandoc --list-output-formats`
