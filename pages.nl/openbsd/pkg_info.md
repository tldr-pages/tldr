# pkg_info

> Bekijk informatie over pakketten in OpenBSD.
> Bekijk ook: `pkg_add`, `pkg_delete`.
> Meer informatie: <https://man.openbsd.org/pkg_info>.

- Zoek naar een pakket met behulp van de pakket-naam:

`pkg_info -Q {{pakket}}`

- Toon een lijst met geïnstalleerde pakketen voor het gebruik met `pkg_add -l`:

`pkg_info -mz`
