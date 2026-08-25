# hledger-ui

> Una interfaz de terminal (TUI) para `hledger`, una aplicación de contabilidad de texto plano robusta y fácil de usar.
> Más información: <https://hledger.org/hledger-ui.html>.

- Se inicia en la pantalla del menú principal, leyendo desde el archivo de diario predeterminado:

`hledger-ui`

- Se inicia con un tema de colores diferente:

`hledger-ui --theme {{terminal|greenterm|dark}}`

- Se inicia con la pantalla de cuentas del balance, mostrando la jerarquía hasta el nivel 3:

`hledger-ui --bs {{[-t|--tree]}} {{[-3|--depth 3]}}`

- Se inicia en la pantalla de la cuenta, mostrando las transacciones liquidadas, y se recarga al producirse un cambio:

`hledger-ui --register {{assets:bank:checking}} {{[-C|--cleared]}} {{[-w|--watch]}}`

- Lee dos archivos de diario y muestra los importes como valor actual cuando se conozca:

`hledger-ui {{[-f|--file]}} {{ruta/a/2024.journal}} {{[-f|--file]}} {{ruta/a/2024-prices.journal}} --value now`

- Muestra el manual en formato Info, si es posible:

`hledger-ui --info`

- Muestra la ayuda:

`hledger-ui {{[-h|--help]}}`
