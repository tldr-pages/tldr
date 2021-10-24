# dep

> Strumento di gestione delle dipendenze per progetti Go.
> Maggiori informazioni: <https://deployer.org>.

- Inizializza la directory corrente come radice di un progetto Go:

`dep init`

- Installa dipendenze mancanti (scannerizza `Gopkg.toml` ed i file `.go`):

`dep ensure`

- Mostra lo stato delle dipendenze di un progetto:

`dep status`

- Aggiungi una dipendenza al progetto:

`dep ensure -add {{url_pacchetto}}`

- Aggiorna le versioni bloccate (in `Gopkg.lock`) di tutte le dipendenze:

`dep ensure -update`
