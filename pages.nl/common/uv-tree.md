# uv tree

> Toon projectafhankelijkheden in een boomstructuur.
> Meer informatie: <https://docs.astral.sh/uv/reference/cli/#uv-tree>.

- Toon afhankelijkheidsboom voor de huidige omgeving:

`uv tree`

- Toon afhankelijkheidsboom voor alle omgevingen:

`uv tree --universal`

- Toon afhankelijkheidsboom tot een bepaalde diepte:

`uv tree {{[-d|--depth]}} {{n}}`

- Toon de nieuwste beschikbare versie voor alle verouderde pakketten:

`uv tree --outdated`

- Sluit afhankelijkheden uit van de dev groep:

`uv tree --no-dev`

- Toon de omgekeerde boom, zodat kinderen afhankelijk zijn in plaats van afhankelijkheden:

`uv tree --invert`
