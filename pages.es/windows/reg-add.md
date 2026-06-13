# reg add

> Agregar nuevas claves y sus valores al registro.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-add>.

- Agregar una nueva clave de registro:

`reg add {{nombre_clave}}`

- Agregar un nuevo [v]alor bajo una clave específica:

`reg add {{nombre_clave}} /v {{valor}}`

- Agregar un nuevo valor con [d]atos específicos:

`reg add {{nombre_clave}} /d {{datos}}`

- Agregar un nuevo valor a una clave con un [t]ipo de dato específico:

`reg add {{nombre_clave}} /t REG_{{SZ|MULTI_SZ|DWORD_BIG_ENDIAN|DWORD|BINARY|DWORD_LITTLE_ENDIAN|LINK|FULL_RESOURCE_DESCRIPTOR|EXPAND_SZ}}`

- [f]orzar (sin un aviso) la sobrescritura del valor de registro existente:

`reg add {{nombre_clave}} /f`
