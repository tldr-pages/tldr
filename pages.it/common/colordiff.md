# colordiff

> Un'utilità per aggiungere colore all'output diff.
> Colordiff è un wrapper scritto in Perl per `diff` e produce lo stesso output, ma con una bella evidenziazione della sintassi. I colori possono essere personalizzati.
> Maggiori informazioni: <https://github.com/kimmel/colordiff>.

- Analisi di due file:

`colordiff {{file1}} {{file2}}`

- Output in due colonne:

`colordiff -y {{file1}} {{file2}}`

- Ignora differenze di maiuscole in file:

`colordiff -i {{file1}} {{file2}}`

- Notifica se file identici:

`colordiff -s {{file1}} {{file2}}`

- Ignora spazio vuoto (white space):

`colordiff -w {{file1}} {{file2}}`
