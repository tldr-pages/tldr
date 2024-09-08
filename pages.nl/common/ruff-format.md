# ruff format

> Een extreem snelle Python code formatter.
> Als geen bestanden of mappen zijn gespecificeerd, wordt de huidige map gebruikt.
> Meer informatie: <https://docs.astral.sh/ruff/formatter>.

- Formateer opgegeven bestanden of mappen in-place:

`ruff format {{pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...}}`

- Toon welke bestanden aangepast zouden worden en return een niet-nul exit code als er bestanden zijn om te formatteren en anders nul:

`ruff format --check`

- Toon welke veranderingen er gemaakt zouden worden zonder de bestanden aan te passen:

`ruff format --diff`
