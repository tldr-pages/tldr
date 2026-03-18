# conda install

> Installa pacchetti in un ambiente conda esistente.  
> Maggiori informazioni: <https://docs.conda.io/projects/conda/en/latest/commands/install.html>.

- Installa uno o più pacchetti nell'ambiente conda attivo:

`conda install {{pacchetto1 pacchetto2 ...}}`

- Installa un singolo pacchetto nell'ambiente conda attivo utilizzando il canale conda-forge:

`conda install {{[-c|--channel]}} conda-forge {{pacchetto}}`

- Installa un singolo pacchetto nell'ambiente conda attivo utilizzando il canale conda-forge e ignorando gli altri canali:

`conda install {{[-c|--channel]}} conda-forge --override-channels {{pacchetto}}`

- Installa una versione specifica di un pacchetto:

`conda install {{pacchetto}}={{versione}}`

- Installa un pacchetto in un ambiente specifico:

`conda install {{[-n|--name]}} {{ambiente}} {{pacchetto}}`

- Aggiorna un pacchetto nell'ambiente attuale:

`conda install --upgrade {{pacchetto}}`

- Installa un pacchetto accettando le modifiche senza richiedere conferma:

`conda install {{[-y|--yes]}} {{pacchetto}}`
