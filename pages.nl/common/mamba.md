# mamba

> Snelle, platformonafhankelijke pakketbeheerder, bedoeld als drop-in vervanging voor conda.
> Sommige subcommando's zoals `repoquery` hebben hun eigen documentatie.
> Zie ook: `conda`.
> Meer informatie: <https://mamba.readthedocs.io/en/latest/user_guide/mamba.html>.

- Maak een nieuwe omgeving aan en installeer hierin de opgegeven pakketten:

`mamba create {{[-n|--name]}} {{omgevingsnaam}} {{python=3.10 matplotlib}}`

- Installeer pakketten in de huidige omgeving, met opgave van het pakketkanaal:

`mamba install {{[-c|--channel]}} {{conda-forge}} {{python=3.6 numpy}}`

- Update alle pakketten in de huidige omgeving:

`mamba update {{[-a|--all]}}`

- Zoek naar een specifiek pakket in alle repositories:

`mamba repoquery search {{numpy}}`

- Toon alle omgevingen:

`mamba info {{[-e|--envs]}}`

- Verwijder ongebruikte pakketten en tarballs uit de cache:

`mamba clean {{[-pt|--packages --tarballs]}}`

- Activeer een omgeving:

`mamba activate {{omgevingsnaam}}`

- Toon alle geïnstalleerde pakketten in de momenteel geactiveerde omgeving:

`mamba list`
