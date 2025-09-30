# uv

> Een snelle Python pakket- en projectbeheerder.
> Sommige subcommando's zoals `tool` en `python` hebben hun eigen documentatie.
> Meer informatie: <https://docs.astral.sh/uv/reference/cli>.

- Creëer een nieuw Python project in de huidige map:

`uv init`

- Creëer een nieuw Python project in het opgegeven pad:

`uv init {{pad/naar/map}}`

- Voeg een nieuwe afhankelijkheid toe aan het project:

`uv add {{pakket}}`

- Verwijder een afhankelijkheid van het project:

`uv remove {{pakket}}`

- Voer een script uit in de projectomgeving:

`uv run {{pad/naar/script.py}}`

- Voer een commando uit in de projectomgeving:

`uv run {{commando}}`

- Update een projectomgeving vanuit `pyproject.toml`:

`uv sync`

- Creëer een lock bestand voor de afhankelijkheden van het project:

`uv lock`
