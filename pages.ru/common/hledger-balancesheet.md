# hledger balancesheet

> Показывать конечные остатки по счетам активов и обязательств.
> Суммы отображаются с обычным положительным знаком, как в стандартной финансовой отчётности.
> Больше информации: <https://hledger.org/hledger.html#balancesheet>.

- Показать текущие остатки по счетам `Asset` и `Liability`, исключая нулевые:

`hledger {{[bs|balancesheet]}}`

- Показать только ликвидные активы (тип счёта `Cash`):

`hledger {{[bs|balancesheet]}} type:C`

- Включить счета с нулевыми остатками и показать иерархию счетов:

`hledger {{[bs|balancesheet]}} {{[-E|--empty]}} {{[-t|--tree]}}`

- Показать остатки на конец каждого месяца:

`hledger {{[bs|balancesheet]}} {{[-M|--monthly]}}`

- Показать рыночную стоимость остатков в базовой валюте на конец каждого месяца:

`hledger {{[bs|balancesheet]}} {{[-M|--monthly]}} {{[-V|--market]}}`

- Показать поквартальные остатки с группировкой до 2-го уровня иерархии счетов:

`hledger {{[bs|balancesheet]}} {{[-Qt|--quarterly --tree]}} {{[-2|--depth 2]}}`

- Показать поквартальные остатки с группировкой до 2-го уровня иерархии счетов и сохранить в HTML-файл `bs.html`:

`hledger {{[bs|balancesheet]}} {{[-Qt|--quarterly --tree]}} {{[-2|--depth 2]}} {{[-o|--output-file]}} bs.html`
