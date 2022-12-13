# poetry

> Verwalte Python-Pakete und -Abhängigkeiten.
> Weitere Informationen: <https://python-poetry.org/docs/cli/>.

- Erstelle ein neues Poetry-Projekt im Verzeichnis mit dem angegebenem Namen:

`poetry new {{projekt_name}}`

- Installiere eine Abhängigkeit und alle Unterabhängigkeiten:

`poetry add {{abhängigkeit}}`

- Installiere eine Entwicklungsabhängigkeit und alle Unterabhängigkeiten:

`poetry add --dev {{abhängigkeit}}`

- Initialisiere ein neues Poetry-Projekt interaktiv im aktuellen Verzeichnis:

`poetry init`

- Aktualisiere alle Abhängigkeiten und `poetry.lock`:

`poetry update`

- Führe einen Befehl innerhalb der virtuellen Umgebung des Projekts aus:

`poetry run {{befehl}}`

- Erhöhe die Minor-Version des Projekts in `pyproject.toml`:

`poetry version minor`

- Liste alle poetry Unterbefehle auf:

`poetry list`
