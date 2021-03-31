# autopep8

> Formatteert automatisch Python-code conform de PEP 8-stijlgids.
> Meer informatie: <https://github.com/hhatto/autopep8>.

- Print het geformatteerde bestand af met een ingestelde maximale toegestane regellengte:

`autopep8 {{pad/naar/bestand.py}} --max-line-length {{len}}`

- Print de diff voor de het geformatteerde bestand:

`autopep8 --diff {{pad/naar/bestand.py}}`

- Formatteer het bestand en sla dit op:

`autopep8 --in-place {{pad/naar/bestand.py}}`

- Formatteer de bestanden recursief in een map en sla dit op:

`autopep8 --in-place --recursive {{pad/naar/map}}`
