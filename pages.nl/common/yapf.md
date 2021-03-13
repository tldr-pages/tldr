# yapf

> Python stijlgidschecker
> Broncode: https://github.com/google/yapf

- Print de geformateerde diff die zal optreden.

`yapf --diff {{pad/naar/bestand}}`

- Print de geformateerde diff af en breng de wijzigingen aan in het bestand.

`yapf --diff --in-place {{pad/naar/bestand}}`

- Formatteer alle Python-bestanden recursief in een map (bijvoorbeeld in pep8-stijl) in parallel.

`yapf --recursive --in-place --style pep8 --parallel {{pad/naar/map}}`
