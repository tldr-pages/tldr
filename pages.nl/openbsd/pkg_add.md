# pkg_add

> Installeer/update pakketten in OpenBSD.
> Bekijk ook: `pkg_info`, `pkg_delete`.
> Meer informatie: <https://man.openbsd.org/pkg_add>.

- Werk alle pakketten bij, inclusief afhankelijkheden:

`pkg_add -u`

- Installeer een nieuw pakket:

`pkg_add {{pakket}}`

- Installeer pakketten van de onbewerkte uitvoer van `pkg_info`:

`pkg_add -l {{pad/naar/file}}`
