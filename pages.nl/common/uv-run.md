# uv run

> Voer een commando of script uit in de projectomgeving.
> Meer informatie: <https://docs.astral.sh/uv/reference/cli/#uv-run>.

- Voer een Python-script uit:

`uv run {{pad/naar/script.py}}`

- Voer een Python-module uit:

`uv run {{[-m|--module]}} {{modulenaam}}`

- Voer een opdracht uit met tijdelijk geïnstalleerde extra pakketten:

`uv run {{[-w|--with]}} {{pakket}} {{commando}}`

- Voer een script uit met pakketten van een requirements-bestand:

`uv run --with-requirements {{pad/naar/requirements.txt}} {{pad/naar/script.py}}`

- Voer uit in een geïsoleerde omgeving (geen projectafhankelijkheden):

`uv run --isolated {{pad/naar/script.py}}`

- Voer uit zonder de omgeving eerste te synchroniseren:

`uv run --no-sync {{commando}}`
