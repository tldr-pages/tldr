# svccfg

> Importeer, exporteer, en wijzig service configurations.
> Meer informatie: <https://www.unix.com/man-page/linux/1m/svccfg>.

- Validatie van een configuratie bestand:

`svccfg validate {{smf.xml}}`

- Exporteer de configuratie van een service naar een bestand:

`svccfg export {{servicename}} > {{smf.xml}}`

- Update de service configuratie aan de hand van een bestand:

`svccfg import {{smf.xml}}`
