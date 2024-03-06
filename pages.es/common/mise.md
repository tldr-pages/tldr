# mise

> Gestiona versiones de diferentes paquetes.
> Más información: <https://mise.jdx.dev>.

- Lista todos los complementos disponibles:

`mise plugins list-all`

- Instala un complemento:

`mise plugins add {{nombre}}`

- Lista las versiones disponibles para instalación:

`mise ls-remote {{nombre}}`

- Instala una versión específica de un paquete:

`mise install {{nombre}}@{{versión}}`

- Establece una versión global de un paquete:

`mise use --global {{nombre}}@{{versión}}`

- Establece una versión local de un paquete:

`mise use {{nombre}}@{{versión}}`

- Establece una variable de entorno en la configuración:

`mise set {{variable}}={{valor}}`
