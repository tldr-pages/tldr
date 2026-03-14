# conda install

> Installa pacchetti in ambiente esistente.
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/latest/commands/install.html>.

- Installa pacchetti ambiente attivo:

`conda install {{pacchetto1 pacchetto2 ...}}`

- Da canale conda-forge:

`conda install {{[-c|--channel]}} conda-forge {{pacchetto}}`

- Solo conda-forge:

`conda install {{[-c|--channel]}} conda-forge --override-channels {{pacchetto}}`

- Versione specifica:

`conda install {{pacchetto}}={{versione}}`

- Ambiente specifico:

`conda install {{[-n|--name]}} {{ambiente}} {{pacchetto}}`

- Aggiorna pacchetto:

`conda install {{[-u|--update]}} {{pacchetto}}`

- Senza conferme:

`conda install {{[-y|--yes]}} {{pacchetto}}`
