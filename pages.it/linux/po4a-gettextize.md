# po4a-gettextize

> Converte un file in un file PO.
> Maggiori informazioni: <https://www.po4a.org/man/man1/po4a-gettextize.1.php>.

- Converte un file di testo in file PO:

`po4a-gettextize --format {{testo}} --master {{percorso/master.txt}} --po {{percorso/risultato.po}}`

- Elenca tutti i formati disponibili:

`po4a-gettextize --help-format`

- Converte un file di testo insieme a un documento tradotto in un file PO (l'opzione `-l` può essere fornita più volte):

`po4a-gettextize --format {{testo}} --master {{percorso/master.txt}} --localized {{percorso/tradotto.txt}} --po {{percorso/risultato.po}}`
