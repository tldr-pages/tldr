# hledger

> Надёжное и удобное приложение для учёта финансов в текстовом формате.
> Смотрите также: `hledger-ui`, `hledger-web`.
> Больше информации: <https://hledger.org/hledger.html>.

- Записать новые транзакции в интерактивном режиме, сохраняя в файл журнала по умолчанию:

`hledger add`

- Импортировать новые транзакции из `bank.csv`, используя `bank.csv.rules` для преобразования:

`hledger import {{путь/к/bank.csv}}`

- Вывести все транзакции, читая из нескольких указанных файлов журнала:

`hledger print {{[-f|--file]}} {{путь/к/prices-2024.journal}} {{[-f|--file]}} {{путь/к/prices-2023.journal}}`

- Показать все счета в виде иерархии и их типы:

`hledger accounts {{[-t|--tree]}} --types`

- Показать балансы счетов активов и обязательств, включая нулевые, в виде иерархии:

`hledger {{[bs|balancesheet]}} {{[-E|--empty]}} {{[-t|--tree]}} --no-elide`

- Показать ежемесячные доходы/расходы/итоги, по убыванию, с группировкой до 2-го уровня:

`hledger {{[is|incomestatement]}} {{[-M|--monthly]}} {{[-T|--row-total]}} {{[-A|--average]}} --sort {{[-2|--depth 2]}}`

- Показать транзакции и текущий баланс счёта `assets:bank:checking`:

`hledger {{[areg|aregister]}} assets:bank:checking`

- Показать сумму расходов на питание со счёта `assets:cash`:

`hledger print assets:cash | hledger {{[-f|--file]}} - {{[-I|--ignore-assertions]}} aregister expenses:food`
