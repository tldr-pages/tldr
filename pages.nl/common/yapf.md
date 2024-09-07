# yapf

> Python stijlgidschecker.
> Meer informatie: <https://github.com/google/yapf>.

- Toon de geformateerde diff die zal optreden uit:

`yapf --diff {{pad/naar/bestand}}`

- Toon de geformateerde diff uit en breng de wijzigingen aan in het bestand:

`yapf --diff --in-place {{pad/naar/bestand}}`

- Formatteer alle Python-bestanden recursief in een map in parallel:

`yapf --recursive --in-place --style {{pep8}} --parallel {{pad/naar/map}}`
