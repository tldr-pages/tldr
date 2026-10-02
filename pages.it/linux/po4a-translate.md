# po4a-translate

> Converte un file PO nel formato di documentazione.
> Il file PO fornito dovrebbe essere la traduzione del file POT prodotto da `po4a-gettextize`.
> Maggiori informazioni: <https://www.po4a.org/man/man1/po4a-translate.1.php>.

- Converte un file PO tradotto in un documento:

`po4a-translate --format {{testo}} --master {{percorso/master.doc}} --po {{percorso/risultato.po}} --localized {{percorso/tradotto.txt}}`

- Elenca tutti i formati disponibili:

`po4a-translate --help-format`
