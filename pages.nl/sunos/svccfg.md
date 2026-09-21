# svccfg

> Importeer, exporteer, en wijzig serviceconfiguraties.
> Meer informatie: <https://www.unix.com/man-page/sunos/1m/svccfg>.

- Valideer een configuratiebestand:

`svccfg validate {{pad/naar/smf_bestand.xml}}`

- Exporteer de configuraties van een service naar een bestand:

`svccfg export {{servicenaam}} > {{pad/naar/smf_bestand.xml}}`

- Importeer/update de serviceconfiguraties vanuit een bestand:

`svccfg import {{pad/naar/smf_bestand.xml}}`
