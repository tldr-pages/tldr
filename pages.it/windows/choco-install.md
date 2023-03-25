# choco install

> Installa uno o più pacchetti con Chocolatey.
> Maggiori informazioni: <https://chocolatey.org/docs/commands-install>

- Installa uno o più pacchetti separati da spazio:

`choco install {{pacchetto1 pacchetto2 ...}}`

- Installa pacchetti da un file di configurazione personalizzato:

`choco install {{percorso\al\file_di_pacchetti.config}}`

- Installa un file nuspec o nupkg specifico:

`choco install {{percorso\al\file}}`

- Installa una nuova versione specifica di un pacchetto:

`choco install {{pacchetto}} --version {{versione}}`

- Consente l'installazione di più versioni di un pacchetto:

`choco install {{pacchetto}} --allow-multiple`

- Conferma automaticamente tutte le richieste:

`choco install {{pacchetto}} --yes`

- Specifica una fonte personalizzata per ricevere pacchetti:

`choco install {{pacchetto}} --source {{url_fonte|alias}}`

- Fornisci un nome utente e una password per l'autenticazione:

`choco install {{pacchetto}} --user {{nome_utente}} --password {{password}}`
