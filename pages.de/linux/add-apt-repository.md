# add-apt-repository

> Verwalte apt-Repository-Definitionen.
> Weitere Informationen: <https://manned.org/apt-add-repository>.

- Füge ein neues apt-Repository hinzu:

`add-apt-repository {{repository_spec}}`

- Entferne ein apt-Repository:

`add-apt-repository --remove {{repository_spec}}`

- Aktualisiere den Paketcache nach dem Hinzufügen eines Repositories:

`add-apt-repository --update {{repository_spec}}`

- Erlaube das Herunterladen von Quellpaketen aus dem Repository:

`add-apt-repository --enable-source {{repository_spec}}`
