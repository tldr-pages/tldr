# dnf

> Paketmanagement Tool für RHEL, Fedora, und CentOS (ersetzt yum).
> Mehr Informationen: <https://dnf.readthedocs.io/>.

- Aktualisierte alle Pakete auf die neuste Version:

`sudo dnf upgrade`

- Sucht nach speziellen Schlüsselwörtern:

`dnf search {{Schlüsselwörter}}`

- Zeigt Daten über das Paket an:

`dnf info {{Paket}}`

- Installiert ein neues Paket:

`sudo dnf install {{Paket}}`

- Installiert ein neues Paket und akzeptiert alles:

`sudo dnf -y install {{Paket}}`

- Entfernt ein Paket:

`sudo dnf remove {{Paket}}`

- Listet alle Pakete:

`dnf list --installed`

- Zeige welches Paket eine Datei hat:

`dnf provides {{Datei}}`
