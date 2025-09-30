# pip

> Python-pakketbeheerder.
> Sommige subcommando's zoals `install` hebben hun eigen documentatie.
> Meer informatie: <https://pip.pypa.io>.

- Installeer een pakket (zie `pip install` voor meer installatievoorbeelden):

`pip install {{pakket}}`

- Installeer een pakket in de directory van de gebruiker in plaats van op de systeembrede standaardlocatie:

`pip install --user {{pakket}}`

- Upgrade een pakket:

`pip install {{[-U|--upgrade]}} {{pakket}}`

- Verwijder een pakket:

`pip uninstall {{pakket}}`

- Sla geïnstalleerde pakketten op in een bestand:

`pip freeze > {{requirements.txt}}`

- Toon informatie over geïnstalleerde pakketten:

`pip show {{pakket}}`

- Installeer pakketten van een bestand:

`pip install {{[-r|--requirement]}} {{requirements.txt}}`
