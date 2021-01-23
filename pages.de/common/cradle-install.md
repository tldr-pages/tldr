# cradle install

> Installiert Cradle PHP Framework Komponenten
> Mehr Informationen: <https://cradlephp.github.io/docs/3.B.-Reference-Command-Line-Tools.html#install>.

- Installieren von Cradle Komponenten (öffnet erst einen Dialog):

`cradle install`

- Gewaltsames Installieren:

`cradle install --force`

- Überspringen von SQL Migrationen:

`cradle install --skip-sql`

- Überspringen von Paket Aktualisierungen:

`cradle install --skip-versioning`

- Benutzer-spezifische Datenbanken Details:

`cradle install -h {{Hostname}} -u {{Benutzer}} -p {{Passwort}}`
