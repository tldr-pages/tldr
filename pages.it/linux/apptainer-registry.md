# apptainer registry

> Gestisce l'autenticazione ai registri OCI/Docker.
> Vedi anche: `apptainer pull`, `apptainer push`.
> Maggiori informazioni: <https://apptainer.org/docs/user/main/cli/apptainer_registry.html>.

- Elenca tutte le credenziali del registro configurate:

`apptainer registry list`

- Accedi a un registro con un nome utente (verrà richiesta la password):

`apptainer registry login {{[-u|--username]}} {{nome_utente}} docker://{{registro}}`

- Accedi a un registro OCI personalizzato:

`apptainer registry login {{[-u|--username]}} {{nome_utente}} oras://{{registro}}`

- Accedi con nome utente e password:

`apptainer registry login {{[-u|--username]}} {{nome_utente}} {{[-p|--password]}} {{password}} docker://{{registro}}`

- Accedi con una password da `stdin`:

`echo "{{password}}" | apptainer registry login {{[-u|--username]}} {{nome_utente}} --password-stdin docker://{{registro}}`

- Accedi utilizzando un file di autenticazione personalizzato:

`apptainer registry login --authfile {{path/to/auth.json}} {{[-u|--username]}} {{nome_utente}} docker://{{registro}}`

- Esci da un registro:

`apptainer registry logout docker://{{registro}}`

- Esci utilizzando un file di autenticazione personalizzato:

`apptainer registry logout --authfile {{path/to/auth.json}} docker://{{registro}}`
