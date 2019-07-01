# cradle install

> Installa i componenti del framework Cradle per PHP.
> Maggiori informazioni: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#install>.

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
