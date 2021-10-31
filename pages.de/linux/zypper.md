# zypper

> SUSE & openSUSE Package Management Werkzeug.
> Weitere Informationen: <https://en.opensuse.org/SDB:Zypper_manual>.

- Synchronisiere Liste von Paketen und verfügbaren Versionen:

`zypper refresh`

- Installiere ein neues Paket:

`zypper install {{paket}}`

- Entferne ein Paket:

`zypper remove {{paket}}`

- Upgrade installierte Pakete zu der neuesten verfügbaren Version:

`zypper update`

- Suche Paket nach einem bestimmten Schema:

`zypper search {{schema}}`

- Zeige Informationen bezüglich der konfigurierten Repositories:

`zypper repos --sort-by-priority`
