# pip freeze

> Toon geïnstalleerde pakketten in requirements-formaat.
> Meer informatie: <https://pip.pypa.io/en/stable/cli/pip_freeze>.

- Toon geïnstalleerde pakketten:

`pip freeze`

- Schrijf geïnstalleerde pakketten naar `requirements.txt`:

`pip freeze > requirements.txt`

- Toon geïnstalleerde pakketten van een virtuele omgeving, met uitzondering van globaal geïnstalleerde pakketten:

`pip freeze {{[-l|--local]}}`

- Toon geïnstalleerde pakketten in de user-site:

`pip freeze --user`

- Toon alle pakketten, inclusief `pip`, `distribute`, `setuptools`, en `wheel` (deze worden normaal overgeslagen):

`pip freeze --all`
