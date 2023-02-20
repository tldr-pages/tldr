# svccfg

> Import, export, and modify service configurations.
> More information: <https://www.unix.com/man-page/linux/1m/svccfg>.

- Validate configuration file:

`svccfg validate {{path/to/smf_file.xml}}`

- Export service configurations to file:

`svccfg export {{servicename}} > {{path/to/smf_file.xml}}`

- Import/update service configurations from file:

`svccfg import {{path/to/smf_file.xml}}`
