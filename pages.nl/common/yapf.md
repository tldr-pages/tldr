# yapf

> Python stijlgidschecker.
> Meer informatie: <https://github.com/google/yapf#usage>.

- Toon een diff van de wijzigingen die gemaakt zouden worden, zonder ze daadwerkelijk te maken (dry-run):

`yapf {{[-d|--diff]}} {{pad/naar/bestand}}`

- Formatteer alle Python-bestanden recursief in een map in parallel:

`yapf {{[-ri|--recursive --in-place]}} --style {{pep8}} {{[-p|--parallel]}} {{pad/naar/map}}`
