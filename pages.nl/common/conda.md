# conda

> Pakket-, afhankelijkheids- en omgevingsbeheer voor alle programmeertalen.
> Sommige subcommando's zoals `create` hebben hun eigen gebruiksdocumentatie.
> Meer informatie: <https://docs.conda.io/projects/conda/en/latest/commands/index.html>.

- Maak een nieuwe omgeving aan en installeer hierin benoemde pakketten:

`conda create {{[-n|--name]}} {{omgevingsnaam}} {{python=3.9 matplotlib}}`

- Toon alle omgevingen:

`conda info {{[-e|--envs]}}`

- Activeer een omgeving:

`conda activate {{omgevingsnaam}}`

- Deactiveer een omgeving:

`conda deactivate`

- Verwijder een omgeving (verwijder alle pakketten):

`conda remove {{[-n|--name]}} {{omgevingsnaam}} --all`

- Installeer pakketten in de huidige omgeving:

`conda install {{python=3.4 numpy}}`

- Toon geïnstalleerde pakketten in de huidige omgeving:

`conda list`

- Verwijder ongebruikte pakketten en caches:

`conda clean {{[-a|--all]}}`
