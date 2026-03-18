# conda update

> Aggiorna i pacchetti all'interno di un ambiente conda, incluso conda stesso.  
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/latest/commands/update.html>.

- Aggiorna tutti i pacchetti nell'ambiente corrente:

`conda update {{[--all|--update-all]}}`

- Aggiorna un pacchetto specifico nell'ambiente corrente:

`conda update {{nome_pacchetto}}`

- Aggiorna conda stesso nell'ambiente base:

`conda update {{[-n|--name]}} base conda`

- Aggiorna i pacchetti ignorando quelli bloccati (pinned):

`conda update --no-pin`

- Aggiorna i pacchetti in modalità offline:

`conda update --offline`
