# hledger balance

> Un informe "sumatorio" flexible y de propósito general que muestra cuentas con algún tipo de dato numérico.
> Puede tratarse de cambios de saldo por periodo, saldos finales, rendimiento presupuestario, plusvalías latentes, etc.
> Más información: <https://hledger.org/hledger.html#balance>.

- Muestra el cambio de saldo en todas las cuentas de todas las contabilizaciones a lo largo de todo el tiempo:

`hledger {{[bal|balance]}}`

- Muestra el cambio de saldo en las cuentas denominadas `*gastos*`, como un árbol, resumiendo solo los dos niveles superiores:

`hledger {{[bal|balance]}} {{gastos}} {{[-t|--tree]}} {{[-2|--depth 2]}}`

- Muestra los gastos de cada mes, y sus totales y medias, ordenados por total; y sus objetivos presupuestarios mensuales:

`hledger {{[bal|balance]}} {{gastos}} {{[-M|--monthly]}} {{[-T|--row-total]}} {{[-A|--average]}} {{[-S|--sort-amount]}} --budget`

- Similar a la anterior, de forma más corta, comparando las cuentas por tipo de `Gastos`, como un árbol de dos niveles sin aplastar las cuentas aburridas:

`hledger {{[bal|balance]}} type:{{X}} {{[-MTAS|--monthly --row-total --average --sort-amount]}} --budget {{[-t|--tree]}} {{[-2|--depth 2]}} --no-elide`

- Muestra saldos finales (incluidos los de contabilizaciones anteriores a la fecha de inicio), trimestrales en 2024, en cuentas denominadas `*activos*` o `*pasivos*`:

`hledger {{[bal|balance]}} {{[-H|--historical]}} {{[-p|--period]}} '{{trimestral en 2024}}' {{activos}} {{pasivos}}`

- Similar al anterior, de un modo más breve; también muestra saldos en cero, ordena por total y resume a tres niveles:

`hledger {{[bal|balance]}} {{[-HQ|--historical --quarterly]}} date:{{2024}} type:{{AL}} {{[-ES|--empty --sort-amount]}} {{[-3|--depth 3]}}`

- Muestra el valor de mercado de los activos de inversión en moneda base al final de cada trimestre:

`hledger {{[bal|balance]}} {{[-HVQ|--historical --market --quarterly]}} {{activos:inversiones}}`

- Muestra las ganancias/pérdidas de capital no realizadas por cambios en el precio de mercado en cada trimestre, para activos de inversión que no sean criptomonedas:

`hledger {{[bal|balance]}} --gain {{[-Q|--quarterly]}} {{activos:inversiones}} not:{{criptomoneda}}`
