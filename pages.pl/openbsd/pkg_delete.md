# pkg_delete

> Usuwanie pakietów w OpenBSD.
> Zobacz także: `pkg_add`, `pkg_info`.
> Więcej informacji: <https://man.openbsd.org/pkg_delete>.

- Usuń pakiet:

`pkg_delete {{pakiet}}`

- Usuń pakiet wraz z jego nieużywanymi zależnościami:

`pkg_delete -a {{pakiet}}`

- Usuwanie pakietu "na sucho":

`pkg_delete -n {{pakiet}}`
