# pkg_delete

> Verwijder pakketten in OpenBSD.
> Bekijk ook: `pkg_add`, `pkg_info`.
> Meer informatie: <https://man.openbsd.org/pkg_delete>.

- Verwijder een pakket:

`pkg_delete {{pakket}}`

- Verwijder een pakket, inclusief de ongebruikte afhankelijkheden:

`pkg_delete -a {{pakket}}`

- Dry-run verwijdering van een pakket:

`pkg_delete -n {{pakket}}`
