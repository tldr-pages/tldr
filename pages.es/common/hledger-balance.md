# hledger balance

> Un informe "sumatorio" flexible y de propósito general que muestra cuentas con algún tipo de dato numérico.
> Puede tratarse de cambios de saldo por periodo, saldos finales, rendimiento presupuestario, plusvalías latentes, etc.
> Más información: <https://hledger.org/hledger.html#balance>.

- Muestra el cambio de saldo en todas las cuentas de todas las contabilizaciones a lo largo de todo el tiempo:

`hledger balance`

- Muestra el cambio de saldo en las cuentas denominadas `*gastos*`, como un árbol, resumiendo solo los dos niveles superiores:

`hledger balance {{gastos}} --tree --depth {{2}}`

- Muestra los gastos de cada mes, y sus totales y medias, ordenados por total; y sus objetivos presupuestarios mensuales:

`hledger balance {{gastos}} --monthly --row-total --average --sort-amount --budget`

- Similar a la anterior, de forma más corta, comparando las cuentas por tipo de `Gastos`, como un árbol de dos niveles sin aplastar las cuentas aburridas:

`hledger bal type:{{X}} -MTAS --budget -t -{{2}} --no-elide`

- Muestra saldos finales (incluidos los de contabilizaciones anteriores a la fecha de inicio), trimestrales en 2024, en cuentas denominadas `*activos*` o `*pasivos*`:

`hledger balance --historical --period '{{trimestral en 2024}}' {{activos}} {{pasivos}}`

- Similar al anterior, de un modo más breve; también muestra saldos en cero, ordena por total y resume a tres niveles:

`hledger bal -HQ date:{{2024}} type:{{AL}} -ES -{{3}}`

- Muestra el valor de mercado de los activos de inversión en moneda base al final de cada trimestre:

`hledger bal -HVQ {{activos:inversiones}}`

- Muestra las ganancias/pérdidas de capital no realizadas por cambios en el precio de mercado en cada trimestre, para activos de inversión que no sean criptomonedas:

`hledger bal --gain -Q {{activos:inversiones}} not:{{criptomoneda}}`
