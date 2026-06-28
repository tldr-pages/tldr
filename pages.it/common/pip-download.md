# pip download

> Scarica pacchetti Python senza installarli.
> Maggiori informazioni: <https://pip.pypa.io/en/stable/cli/pip_download/>.

- Scarica un file wheel o un archivio sorgente di un pacchetto nella directory corrente:

`pip download {{pacchetto}}`

- Scarica una versione specifica di un pacchetto:

`pip download {{pacchetto}}=={{versione}}`

- Scarica un pacchetto e le sue dipendenze in una directory specifica:

`pip download {{pacchetto}} {{[-d|--dest]}} {{percorso/della/directory}}`

- Scarica un pacchetto per una specifica piattaforma e versione di Python:

`pip download {{pacchetto}} --only-binary :all: --platform {{piattaforma}} --python-version {{versione}}`

- Scarica un pacchetto da un URL di indice specifico:

`pip download {{pacchetto}} {{[-i|--index-url]}} {{url}}`
