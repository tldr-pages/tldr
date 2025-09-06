# autopep8

> Formatteer Python-code conform de PEP 8-stijlgids.
> Meer informatie: <https://github.com/hhatto/autopep8>.

- Formateer een bestand naar `stdout`, met een ingestelde maximale toegestane regellengte:

`autopep8 {{pad/naar/bestand.py}} --max-line-length {{lengte}}`

- Formateer een bestand, geef een diff weer met de wijzigingen:

`autopep8 --diff {{pad/naar/bestand.py}}`

- Formatteer het bestand en sla de wijzigingen op:

`autopep8 --in-place {{pad/naar/bestand.py}}`

- Formatteer de bestanden recursief in een map en sla deze wijzigingen op:

`autopep8 --in-place --recursive {{pad/naar/map}}`
