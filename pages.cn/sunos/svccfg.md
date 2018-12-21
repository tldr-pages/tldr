# svccfg

> Import, export, and modify service configurations.

- Validate configuration file:

`svccfg validate {{smf.xml}}`

- Export service configurations to file:

`svccfg export {{servicename}} > {{smf.xml}}`

- Import/update service configurations from file:

`svccfg import {{smf.xml}}`
