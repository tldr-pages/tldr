# tlmgr

> Verwalte Packages und Konfigurationen einer existierenden TeX Live Installation.
> Manche Unterbefehle wie `tlmgr paper` sind separat dokumentiert.
> Weitere Informationen: <https://www.tug.org/texlive/tlmgr.html>.

- Installiere ein Package und seine Abhängigkeiten:

`tlmgr install {{package}}`

- Entferne ein Package und seine Abhängigkeiten:

`tlmgr remove {{package}}`

- Zeige Informationen über ein Package an:

`tlmgr info {{package}}`

- Aktualisiere alle Packages:

`tlmgr update --all`

- Zeige mögliche Aktualisierungen an, ohne Änderungen vorzunehmen:

`tlmgr update --list`

- Starte die grafische Oberfläche von tlmgr:

`tlmgr gui`

- Liste alle Tex Live Konfigurationen auf:

`tlmgr conf`
