# csvformat

> Converti un file CSV in un formato di output personalizzato.
> Incluso in csvkit.
> Maggiori informazioni: <https://csvkit.readthedocs.io/en/latest/scripts/csvformat.html>.

- Converti in un file delimitato da tab (TSV):

`csvformat {{[-T|--out-tabs]}} {{dati.csv}}`

- Converti i delimitatori in un carattere personalizzato:

`csvformat {{[-D|--out-delimiter]}} "{{carattere_personalizzato}}" {{dati.csv}}`

- Converti caratteri newline a carriage return (^M) + newline:

`csvformat {{[-M|--out-lineterminator]}} "{{\r\n}}" {{dati.csv}}`

- Minimizza l'utilizzo delle virgolette:

`csvformat {{[-U|--out-quoting]}} 0 {{dati.csv}}`

- Massimizza l'utilizzo delle virgolette:

`csvformat {{[-U|--out-quoting]}} 1 {{dati.csv}}`
