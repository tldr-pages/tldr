# fdroid

> F-Droid Build Tool.
> F-Droid ist ein installierbarer Katalog mit FOSS (Freie Open Source Software) Apps für Android.
> Weitere Informationen: <https://f-droid.org/en/docs/Building_Applications/>.

- Kompiliere eine bestimmte App:

`fdroid build {{app_id}}`

- Kompiliere eine bestimmte App in einer Build-Server-VM:

`fdroid build {{app_id}} --server`

- Veröffentliche die App im lokalen Repository:

`fdroid publish {{app_id}}`

- Installiere die App auf jedem verbundenen Gerät:

`fdroid install {{app_id}}`

- Überprüfe, ob die Metadaten korrekt formatiert sind:

`fdroid lint --format {{app_id}}`

- Korrigiere die Formatierung automatisch (wenn möglich):

`fdroid rewritemeta {{app_id}}`
