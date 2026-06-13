# hledger

> Una aplicación de contabilidad en texto plano que es robusta y fácil de usar.
> Vea también: `hledger-ui`, `hledger-web`.
> Más información: <https://hledger.org/hledger.html>.

- Registra nuevas transacciones interactivamente, guardándolas en el archivo de diario por defecto:

`hledger add`

- Importa nuevas transacciones de `banco.csv`, usando `banco.csv.rules` para convertir:

`hledger import {{ruta/a/banco.csv}}`

- Imprime todas las transacciones, leyendo múltiples archivos de diario específicos:

`hledger print {{[-f|--file]}} {{ruta/a/precios-2024.journal}} {{[-f|--file]}} {{ruta/a/precios-2023.journal}}`

- Muestra todas las cuentas, como jerarquía, y sus tipos:

`hledger accounts {{[-t|--tree]}} --types`

- Muestra saldos de cuenta de activos y pasivos, incluyendo ceros, jerárquicamente:

`hledger {{[bs|balancesheet]}} {{[-E|--empty]}} {{[-t|--tree]}} --no-elide`

- Muestra ingresos/gastos/totales mensuales, los más grandes primero, resumido a 2 niveles:

`hledger {{[is|incomestatement]}} {{[-M|--monthly]}} {{[-T|--row-total]}} {{[-A|--average]}} --sort {{[-2|--depth 2]}}`

- Muestra las transacciones de la cuenta `assets:bank:checking` y su saldo actual:

`hledger {{[areg|aregister]}} assets:bank:checking`

- Muestra el monto gastado en comida desde la cuenta `assets:cash`:

`hledger print assets:cash | hledger {{[-f|--file]}} - {{[-I|--ignore-assertions]}} aregister expenses:food`
