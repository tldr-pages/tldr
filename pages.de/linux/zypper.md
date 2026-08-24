# zypper

> SUSE & openSUSE Package-Management-Werkzeug.
> Weitere Informationen: <https://en.opensuse.org/SDB:Zypper_manual>.

- Synchronisiere die Liste von Paketen und verfügbaren Versionen:

`sudo zypper {{[ref|refresh]}}`

- Installiere ein neues Paket:

`sudo zypper {{[in|install]}} {{paket}}`

- Entferne ein Paket:

`sudo zypper {{[rm|remove]}} {{paket}}`

- Aktualisiere installierte Pakete zur neuesten verfügbaren Version:

`sudo zypper {{[up|update]}}`

- Suche Paket nach einem bestimmten Schema:

`zypper {{[se|search]}} {{schema}}`

- Zeige Informationen bezüglich der konfigurierten Repositories:

`zypper {{[lr|repos]}} --sort-by-priority`
