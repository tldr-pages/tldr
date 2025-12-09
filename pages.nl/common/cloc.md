# cloc

> Tel het aantal regels code.
> Meer informatie: <https://github.com/AlDanial/cloc#options->.

- Tel alle regels code in een map:

`cloc {{pad/naar/map}}`

- Vergelijk twee mapstructuren en tel de verschillen ertussen:

`cloc --diff {{pad/naar/map1}} {{pad/naar/map2}}`

- Negeer bestanden die door de VCS worden genegeerd, zoals bestanden die in `.gitignore` staan:

`cloc --vcs git {{pad/naar/map}}`

- Toon de resultaten voor elk bestand in plaats van elke taal:

`cloc --by-file {{pad/naar/map}}`
