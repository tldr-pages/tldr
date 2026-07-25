# choco

> El gestor de paquetes Chocolatey.
> Algunos subcomandos, como `install`, `upgrade` y `pin`, cuentan con su propia documentación de uso.
> Más información: <https://docs.chocolatey.org/en-us/choco/commands/>.

- Instala un paquete:

`choco install {{nombre_del_paquete}}`

- Actualiza un paquete específico ya instalado:

`choco upgrade {{nombre_del_paquete}}`

- Actualiza todos los paquetes obsoletos y confirma automáticamente todas las solicitudes:

`choco upgrade all {{[-y|--yes]}}`

- Desinstala un paquete y confirma automáticamente todas las solicitudes:

`choco uninstall {{nombre_del_paquete}} {{[-y|--yes]}}`

- Busca paquetes por nombre o palabra clave:

`choco search {{consulta}}`

- Muestra todos los paquetes instalados en el equipo:

`choco list`

- Muestra los paquetes para los que hay versiones más recientes disponibles:

`choco outdated`

- Instala un paquete desde una fuente específica:

`choco install {{nombre_del_paquete}} {{[-s|--source]}} {{fuente}}`
