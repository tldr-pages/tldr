# svccfg

> Importă, exportă și modifică configurațiile serviciilor.
> Mai multe informații: <https://www.unix.com/man-page/linux/1m/svccfg>.

- Validează un fișier de configurare:

`svccfg validate {{cale/către/fișier_smf.xml}}`

- Exportă configurațiile serviciului într-un fișier:

`svccfg export {{nume_serviciu}} > {{cale/către/fișier_smf.xml}}`

- Importă/actualizează configurațiile serviciului dintr-un fișier:

`svccfg import {{cale/către/fișier_smf.xml}}`
