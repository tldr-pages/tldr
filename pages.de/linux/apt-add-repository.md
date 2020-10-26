# apt-add-repository

> Editiere die Repository-Listen.

- Fügt ein neues Repository hinzu:

`apt-add-repository {{repository_spec}}`

- Entfernt ein Repository:

`apt-add-repository --remove {{repository_spec}}`

- Aktualisiert den Cache nachdem das Repository hinzugefügt wurde:

`apt-add-repository --update {{repository_spec}}`

- Aktiviert Source Pakete:

`apt-add-repository --enable-source {{repository_spec}}`
