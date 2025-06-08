# uv add

> Voeg pakket afhankelijkheden toe aan het `pyproject.toml` bestand.
> Pakketten worden gespecificeerd volgens <https://peps.python.org/pep-0508/>.
> Meer informatie: <https://docs.astral.sh/uv/reference/cli/#uv-add>.

- Voeg de nieuwste versie van een pakket toe:

`uv add {{pakket}}`

- Voeg meerdere pakketten toe:

`uv add {{pakket1 pakket2 ...}}`

- Voeg een pakket toe met een versievereiste:

`uv add {{pakket>=1.2.3}}`

- Voeg pakketten toe aan een optionele afhankelijkheidsgroep, die wordt opgenomen wanneer ze worden gepubliceerd:

`uv add --optional {{optioneel}} {{pakket1 pakket2 ...}}`

- Voeg pakketten toe aan een lokale groep, die niet wordt opgenomen wanneer ze worden gepubliceerd:

`uv add --group {{groep}} {{pakket1 pakket2 ...}}`

- Voeg pakketten toe aan de dev groep, afkorting voor `--group dev`:

`uv add --dev {{pakket1 pakket2 ...}}`

- Voeg pakket toe als bewerkbaar:

`uv add --editable {{pad/naar/pakket/}}`

- Schakel een extra in bij het installeren van een pakket, deze kan meerdere keren opgegeven worden:

`uv add {{pakket}} --extra {{extra_functie}}`
