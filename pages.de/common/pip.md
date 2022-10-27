# pip

> Python package manager.
> Einige Unterbefehle wie `pip install` sind separat dokumentiert.
> Weitere Informationen: <https://pip.pypa.io>.

- Installiere ein Paket (siehe `pip install` für weitere Beispiele):

`pip install {{paketname}}`

- Installiere ein Paket im Benutzerverzeichnis, anstatt systemweit:

`pip install --user {{paketname}}`

- Aktualisiere ein Paket:

`pip install --upgrade {{paketname}}`

- Deinstalliere ein Paket:

`pip uninstall {{paketname}}`

- Speichere eine Liste aller installierten Pakete in eine Datei:

`pip freeze > {{requirements.txt}}`

- Zeige Informationen über ein installiertes Paket an:

`pip show {{paketname}}`

- Installiere Pakete, die in einer Datei gelistet sind:

`pip install --requirement {{requirements.txt}}`
