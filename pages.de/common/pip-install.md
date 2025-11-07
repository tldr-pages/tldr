# pip install

> Installiere Python-Pakete.
> Weitere Informationen: <https://pip.pypa.io/en/stable/cli/pip_install/>.

- Installiere ein Paket:

`pip install {{paketname}}`

- Installiere eine spezifische Paketversion:

`pip install {{paketname}}=={{paketversion}}`

- Installiere die Pakete aus einer Datei:

`pip install {{[-r|--requirement]}} {{requirements.txt}}`

- Installiere die Pakete von einer URL oder einem lokalen Archiv (.tar.gz | .whl):

`pip install {{[-f|--find-links]}} {{url|pfad/zu/datei}}`

- Installiere das lokale Paket im aktuellen Verzeichnis im Entwicklungs-/Bearbeitungsmodus:

`pip install {{[-e|--editable]}} .`
