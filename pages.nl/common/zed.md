# zed

> Tekstverwerker ontworpen om snel, efficiënt en handig te zijn.
> Meer informatie: <https://zed.dev/docs/#cli>.

- Open specifieke paden in Zed:

`zed {{pad/naar/bestand_of_map1 pad/naar/bestand_of_map2 ...}}`

- Open een pad op de voorgrond en toon logs:

`zed {{pad/naar/project}} --foreground`

- Open een pad in een nieuw venster:

`zed {{pad/naar/project}} {{[-n|--new]}}`

- Open een bestand op het opgegeven regelnummer en kolom:

`zed {{pad/naar/bestand}}:{{regelnummer}}:{{kolomnummer}}`

- Toon een diff in Zed voor twee versies van een bestand:

`zed --diff {{pad/naar/oud_bestand}} {{pad/naar/nieuw_bestand}}`
