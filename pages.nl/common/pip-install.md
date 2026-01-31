# pip install

> Installeer Python-pakketten.
> Meer informatie: <https://pip.pypa.io/en/stable/cli/pip_install/>.

- Installeer één of meer pakketten:

`pip install {{pakket1 pakket2 ...}}`

- Upgrade alle opgegeven pakketten naar de nieuwste versie en installeer alle pakketten die nog niet aanwezig zijn:

`pip install {{pakket1 pakket2 ...}} {{[-U|--upgrade]}}`

- Installeer een specifieke versie van een pakket:

`pip install {{pakket}}=={{versie}}`

- Installeer pakketten die in een bestand staan:

`pip install {{[-r|--requirement]}} {{pad/naar/requirements.txt}}`

- Installeer pakketten vanaf een URL of lokaal bestandsarchief (bijv. `.tar.gz` of `.whl`):

`pip install {{[-f|--find-links]}} {{url|pad/naar/bestand}}`

- Installeer het lokale pakket in de huidige map in develop-modus:

`pip install {{[-e|--editable]}} .`
