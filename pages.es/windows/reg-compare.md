# reg compare

> Comparar claves y sus valores en el registro.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-compare>.

- Comparar todos los valores bajo una clave específica con otra clave:

`reg compare {{nombre_clave1}} {{nombre_clave2}}`

- Comparar un [v]alor específico bajo dos claves:

`reg compare {{nombre_clave1}} {{nombre_clave2}} /v {{valor}}`

- Comparar todos los [s]ubclaves y valores para dos claves:

`reg compare {{nombre_clave1}} {{nombre_clave2}} /s`

- Solo [o]utputear las coincidencias ([s]imilares) entre las claves especificadas:

`reg compare {{nombre_clave1}} {{nombre_clave2}} /os`

- [o]utputear las diferencias y coincidencias ([a]mbas) entre las claves especificadas:

`reg compare {{nombre_clave1}} {{nombre_clave2}} /oa`

- Comparar dos claves, [o]utputando [n]ada:

`reg compare {{nombre_clave1}} {{nombre_clave2}} /on`
