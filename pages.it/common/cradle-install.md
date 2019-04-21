# cradle install

> Installa i componenti del framework Cradle per PHP.

- Installa i componenti di Cradle (maggiori dettagli verranno richiesti all'utente):

`cradle install`

- Sovrascrivi i file forzatamente:

`cradle install --force`

- Salta l'esecuzione di migrazioni SQL:

`cradle install --skip-sql`

- Salta l'esecuzione di aggiornamenti dei pacchetti:

`cradle install --skip-versioning`

- Utilizza specifici dettagli per il database:

`cradle install -h {{hostname}} -u {{nome_utente}} -p {{password}}`
