# hledger

> Una aplicación de contabilidad en texto plano que es robusta y fácil de usar.
> Vea también: `hledger-ui` para la TUI, `hledger-web` para la interfaz web.
> Más información: <https://hledger.org/hledger.html>.

- Registra nuevas transacciones interactivamente, guardándolas en el archivo de diario por defecto:

`hledger add`

- Importa nuevas transacciones de `banco.csv`, usando `banco.csv.rules` para convertir:

`hledger import {{ruta/a/banco.csv}}`

- Imprime todas las transacciones, leyendo múltiples archivos de diario específicos:

`hledger print --file {{ruta/a/precios-2024.journal}} --file {{ruta/a/precios-2023.journal}}`

- Muestra todas las cuentas, como jerarquía, y sus tipos:

`hledger accounts --tree --types`

- Muestra saldos de cuenta de activos y pasivos, incluyendo ceros, jerárquicamente:

`hledger balancesheet --empty --tree --no-elide`

- Muestra ingresos/gastos/totales mensuales, los más grandes primero, resumido a 2 niveles:

`hledger incomestatement --monthly --row-total --average --sort --depth 2`

- Muestra las transacciones de la cuenta `assets:bank:checking` y su saldo actual:

`hledger aregister assets:bank:checking`

- Muestra el monto gastado en comida desde la cuenta `assets:cash`:

`hledger print assets:cash | hledger -f- -I aregister expenses:food`
