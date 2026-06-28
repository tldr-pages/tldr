# pip inspect

> Ispeziona l'ambiente Python e produci un rapporto in formato JSON.
> Maggiori informazioni: <https://pip.pypa.io/en/stable/cli/pip_inspect/>.

- Ispeziona l'ambiente corrente:

`pip inspect`

- Ispeziona e salva l'output in un file:

`pip inspect > {{environment_report.json}}`

- Ispeziona solo i pacchetti installati localmente (non globali):

`pip inspect --local`

- Ispeziona solo i pacchetti installati dall'utente:

`pip inspect --user`

- Ispeziona i pacchetti in uno specifico percorso:

`pip inspect --path {{percorso/dell/ambiente}}`

- Ispeziona con un output dettagliato (Nota: il flag `-v` può essere ripetuto per aumentare la verbosità):

`pip inspect {{[-v|--verbose]}}`
