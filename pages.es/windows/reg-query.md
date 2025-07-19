# reg query

> Muestra los valores de claves y subclaves en el registro.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/reg-query>.

- Muestra todos los valores de una clave:

`reg query {{nombre_de_clave}}`

- Muestra un [v]alor específico de una clave:

`reg query {{nombre_de_clave}} /v {{valor}}`

- Mostrar todos los valores de una clave y sus [s]ubclaves:

`reg query {{nombre_de_clave}} /s`

- Buscar [f] claves y valores que coincidan con un patrón específico:

`reg query {{nombre_de_clave}} /f "{{patrón_de_búsqueda}}"`

- Mostrar un valor de una clave que coincida con un [t]ipo de dato específico:

`reg query {{nombre_de_clave}} /t REG_{{SZ|MULTI_SZ|EXPAND_SZ|DWORD|BINARY|NONE}}`

- Buscar solo en los [d]atos:

`reg query {{nombre_de_clave}} /d`

- Buscar solo en los nombres de clave [k]:

`reg query {{nombre_de_clave}} /f "{{patrón_de_búsqueda}}" /k`

- Buscar una coincidencia [e]xacta distinguiendo entre mayúsculas y minúsculas [c]:

`reg query {{nombre_de_clave}} /c /e`
