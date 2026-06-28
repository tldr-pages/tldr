# pip install

> Installa pacchetti Python.
> Maggiori informazioni: <https://pip.pypa.io/en/stable/cli/pip_install/>.

- Installa uno o più pacchetti:

`pip install {{pacchetto1 pacchetto2 ...}}`

- Aggiorna tutti i pacchetti specificati all'ultima versione, installando anche quelli non ancora presenti:

`pip install {{pacchetto1 pacchetto2 ...}} {{[-U|--upgrade]}}`

- Installa una versione specifica di un pacchetto:

`pip install {{pacchetto}}=={{versione}}`

- Installa i pacchetti elencati in un file:

`pip install {{[-r|--requirement]}} {{percorso/del/requirements.txt}}`

- Installa un pacchetto da un archivio locale o da una directory:

`pip install {{percorso/del/file.whl|percorso/del/file.tar.gz|percorso/della/directory}}`

- Installa un pacchetto da un repository Git:

`pip install git+https://{{esempio.com}}/{{nome_utente}}/{{repository}}.git`

- Installa un pacchetto da una sorgente alternativa (URL o directory) invece che da PyPI:

`pip install {{[-f|--find-links]}} {{url|percorso/della/directory}} {{pacchetto}}`

- Installa il pacchetto locale nella directory corrente in modalità sviluppo (modificabile):

`pip install {{[-e|--editable]}} .`
