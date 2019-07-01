# csvformat

> Converti un file CSV in un formato di output personalizzato.
> Incluso in csvkit.
> Maggiori informazioni: <https://csvkit.readthedocs.io/en/latest/scripts/csvformat.html>.

- Converti in un file delimitato da tab (TSV):

`csvformat -T {{dati.csv}}`

- Converti i delimitatori in un carattere personalizzato:

`csvformat -D "{{carattere_personalizzato}}" {{dati.csv}}`

- Converti caratteri newline a carriage return (^M) + newline:

`csvformat -M "{{\r\n}}" {{dati.csv}}`

- Minimizza l'utilizzo delle virgolette:

`csvformat -U 0 {{dati.csv}}`

- Massimizza l'utilizzo delle virgolette:

`csvformat -U 1 {{dati.csv}}`
