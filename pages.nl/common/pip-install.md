# pip install

> Installeer Python-pakketten.
> Meer informatie: <https://pip.pypa.io/en/stable/cli/pip_install/>.

- Installeer een pakket:

`pip install {{pakket}}`

- Installeer een specifieke versie van een pakket:

`pip install {{pakket}}=={{versie}}`

- Installeer pakketten die in een bestand staan:

`pip install {{[-r|--requirement]}} {{pad/naar/requirements.txt}}`

- Installeer pakketten vanaf een URL of lokaal bestandsarchief (bijv. `.tar.gz` of `.whl`):

`pip install {{[-f|--find-links]}} {{url|pad/naar/bestand}}`

- Installeer het lokale pakket in de huidige map in develop-modus:

`pip install {{[-e|--editable]}} .`
