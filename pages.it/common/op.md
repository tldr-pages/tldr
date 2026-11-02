# op

> CLI ufficiale per l'app desktop di 1Password.
> Maggiori informazioni: <https://developer.1password.com/docs/cli/reference/>.

- Accedi a un account 1Password:

`op signin`

- Elenca tutte le casseforti:

`op vault list`

- Mostra i dettagli di un elemento in formato JSON:

`op item get {{nome_elemento}} --format json`

- Crea un nuovo elemento di una categoria nella cassaforte predefinita:

`op item create --category {{nome_categoria}}`

- Stampa un segreto referenziato su `stdout`:

`op read {{riferimento_segreto}}`

- Passa a un comando i riferimenti ai segreti dalle variabili d'ambiente esportate:

`op run -- {{comando}}`

- Passa a un comando i riferimenti ai segreti da un file di ambiente:

`op run --env-file {{percorso/del/file_env.env}} -- {{comando}}`

- Leggi i riferimenti ai segreti da un file e salva i segreti in chiaro in un altro file:

`op inject --in-file {{percorso/del/file_input}} --out-file {{percorso/del/file_output}}`
