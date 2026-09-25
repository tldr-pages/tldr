# reg copy

> Copia claves y sus valores en el registro.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-copy>.

- Copia una clave de registro a una nueva ubicación de registro:

`reg copy {{nombre_clave_antigua}} {{nombre_clave_nueva}}`

- Copia una clave de registro recursivamente (con todas las [s]ubclaves) a una nueva ubicación de registro:

`reg copy {{nombre_clave_antigua}} {{nombre_clave_nueva}} /s`

- [f]uerza (sin un aviso) la copia de una clave de registro:

`reg copy {{nombre_clave_antigua}} {{nombre_clave_nueva}} /f`
