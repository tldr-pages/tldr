# svccfg

> Import, export, and modify service configurations

- validate configuration file

`svccfg validate {{smf.xml}}`

- export service configurations to file

`svccfg export {{servicename}} > {{smf.xml}}`

- import/update service configurations from file.

`svccfg import {{smf.xml}}`
