# uv init

> Creëer een nieuw Python project.
> Meer informatie: <https://docs.astral.sh/uv/reference/cli/#uv-init>.

- Initialiseer een project in de huidige map:

`uv init`

- Initialiseer een project met een gegeven naam:

`uv init {{project_naam}}`

- Creëer een project in een bepaalde map:

`uv init --directory {{pad/naar/map}} {{project_naam}}`

- Creëer een project voor een Python library:

`uv init {{[--lib|--library]}} {{project_naam}}`

- Specificeer het bouwsysteem:

`uv init --build-backend {{bouwsysteem}} {{project_naam}}`

- Creëer alleen een `pyproject.toml`:

`uv init --bare {{project_naam}}`

- Specificeer de projectbeschrijving:

`uv init --description "{{omschrijving}}" {{project_naam}}`
