# aptitude

> Debian und Ubuntu Paket Management Tool.
> Weitere Informationen: <https://manpages.debian.org/latest/aptitude/aptitude.8.html>.

- Synchronisiere die Paketliste und verfügbaren Versionen. Dieser Command sollte zuerst ausgeführt werden bevor weitere aptitude Commands ausgeführt werden:

`aptitude update`

- Installiere ein neues Paket und seine Abhängigkeiten:

`aptitude install {{paket}}`

- Suche nach einem Paket:

`aptitude search {{paket}}`

- Suche nach einem installierten Paket (`?installed` ist ein aptitude Suchbegriff):

`aptitude search '?installed ({{paket}})'`

- Entferne ein Paket und alle Abhängigkeiten:

`aptitude remove {{paket}}`

- Aktualisiere installierte Pakete auf die neusten Versionen:

`aptitude upgrade`

- Aktualisiere installierte Pakete (wie `aptitude upgrade`), inklusive obsoleter Pakete und installiere zusätzliche Pakete um die neuen Paket-Abhängigkeiten zu erfüllen:

`aptitude full-upgrade`

- Friere ein installiertes Paket ein und verhindere, dass es automatisch aktualisiert wird:

`aptitude hold '?installed({{paket}})'`
