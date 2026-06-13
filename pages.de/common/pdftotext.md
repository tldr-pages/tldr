# pdftotext

> Konvertiere PDF Dateien zum plain text Format.
> Weitere Informationen: <https://www.xpdfreader.com/pdftotext-man.html>.

- Konvertiere `datei.pdf` zu plain text und gib sie über die Standardausgabe aus:

`pdftotext {{datei.pdf}} -`

- Konvertiere `datei.pdf` zu plain text und speichere sie als `datei.txt`:

`pdftotext {{datei.pdf}}`

- Konvertiere `datei.pdf` zu plain text und erhalte das Layout:

`pdftotext -layout {{datei.pdf}}`

- Konvertiere `quelldatei.pdf` zu plain text und speichere sie als `zieldatei.txt`:

`pdftotext {{quelldatei.pdf}} {{zieldatei.txt}}`

- Konvertiere Seite 2, 3 und 4 von `quelldatei.pdf` zu plain text und speichere sie als `zieldatei.txt`:

`pdftotext -f {{2}} -l {{4}} {{quelldatei.pdf}} {{zieldatei.txt}}`
