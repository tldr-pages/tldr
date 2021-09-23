# dnf

> Paketmanagement Tool für RHEL, Fedora, und CentOS (ersetzt yum).
> Weitere Informationen: <https://dnf.readthedocs.io>.

- Aktualisiere alle Pakete auf die neueste Version:

`sudo dnf upgrade`

- Suche nach Paketen:

`dnf search {{schlüsselwort}}`

- Zeige Daten über ein bestimmtes Paket an:

`dnf info {{paket}}`

- Installiere ein neues Paket:

`sudo dnf install {{paket}}`

- Installiere ein neues Paket und antworte "ja" auf alle Fragen:

`sudo dnf -y install {{paket}}`

- Entferne ein Paket:

`sudo dnf remove {{paket}}`

- Liste alle Pakete auf:

`dnf list --installed`

- Zeige welches Paket eine Datei besitzt:

`dnf provides {{pfad/zu/datei}}`
