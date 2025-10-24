# yapf

> Python stijlgidschecker.
> Meer informatie: <https://github.com/google/yapf>.

- Toon de geformatteerde diff die zal optreden uit:

`yapf {{[-d|--diff]}} {{pad/naar/bestand}}`

- Formatteer alle Python-bestanden recursief in een map in parallel:

`yapf {{[-ri|--recursive --in-place]}} --style {{pep8}} {{[-p|--parallel]}} {{pad/naar/map}}`
