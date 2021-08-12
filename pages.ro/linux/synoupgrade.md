# synoupgrade

> Faceți upgrade unui Synology DiskStation Manager (DSM) din linia de comandă.
> Mai multe informaţii: <https://www.synology.com/dsm>

- Verificați dacă sunt disponibile upgrade-uri:

`sudo synoupgrade --check`

- Verificați pentru patch-uri fără a actualiza versiunea DSM:

`sudo synoupgrade --check-smallupdate`

- Descărcați cea mai recentă actualizare disponibilă (utilizați `—download-smallupdate` pentru patch-uri):

`sudo synoupgrade --download`

- Porniți procesul de actualizare:

`sudo synoupgrade --start`

- Upgrade automat la cea mai recentă versiune:

`sudo synoupgrade --auto`

- Aplicați corecții fără actualizarea automată a versiunii DSM:

`sudo synoupgrade --auto-smallupdate`

- Upgrade DSM folosind un fișier de patch-uri (ar trebui să fie o cale absolută):

`sudo synoupgrade --patch {{/path/to/file.pat}}`

- Ajutor pentru afișare:

`synoupgrade`
