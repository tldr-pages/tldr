# reg delete

> Elimina claves o sus valores del registro.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-delete>.

- Elimina una clave de registro específica:

`reg delete {{nombre_clave}}`

- Elimina un [v]alor bajo una clave específica:

`reg delete {{nombre_clave}} /v {{valor}}`

- Elimina todos [a] los [v]alores recursivamente bajo la clave especificada:

`reg delete {{nombre_clave}} /va`

- [f]orzar (sin un aviso) la eliminación de todos [a] los [v]alores recursivamente bajo una clave:

`reg delete {{nombre_clave}} /f /va`
