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

- Installeer een pakket van een lokaal archief of map:

`pip install {{pad/naar/bestand.whl|pad/naar/bestand.tar.gz|pad/naar/map}}`

- Installeer een pakket van een Git-repository:

`pip install git+https://{{example.com}}/{{gebruiker}}/{{repository}}.git`

- Installeer een pakket van een alternatieve bron (URL of map) in plaats van PyPI:

`pip install {{[-f|--find-links]}} {{url|pad/naar/map}} {{pakket}}`

- Installeer het lokale pakket in de huidige map in develop-modus:

`pip install {{[-e|--editable]}} .`
