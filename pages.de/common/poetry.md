# poetry

> Verwalte Python-Paketen und -Abhängigkeiten.
> Weitere Informationen: <https://python-poetry.org/docs/cli/>.

- Erstellen eins neuen Poetry-Projekts im Verzeichnis mit dem angegebenem Namen:

`poetry new {{projekt_name}}`

- Installation einer Abhängigkeit und allen Unterabhängigkeiten:

`poetry add {{abhängigkeit}}`

- Installation einer Entwicklungsabhängigkeit und allen Unterabhängigkeiten:

`poetry add --dev {{abhängigkeit}}`

- Interaktives Initialisieren eines neuen Poetry-Projekts im aktuellen Verzeichnis:

`poetry init`

- Aktualisieren aller Abhängigkeiten und `poetry.lock` aktualisieren:

`poetry update`

- Einen Befehl innerhalb der virtuellen Umgebung des Projekts ausführen:

`poetry run {{befehl}}`

- Die Minor-Version des projects in `pyproject.toml` erhöhen:

`poetry version minor`

- Alle poetry Unterbefehle auflisten:

`poetry list`
