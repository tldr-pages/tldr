# apt-add-repository

> Editiere die Repository-Listen.
> Weitere Informationen: <https://manpages.debian.org/latest/software-properties-common/apt-add-repository.1.html>.

- Füge ein neues Repository hinzu:

`apt-add-repository {{repository_spec}}`

- Entferne ein Repository:

`apt-add-repository --remove {{repository}}`

- Aktualisiere den Cache nachdem das Repository hinzugefügt wurde:

`apt-add-repository --update {{repository}}`

- Aktiviere Source-Pakete:

`apt-add-repository --enable-source {{repository}}`
