# hledger aregister

> Показывать транзакции и текущий баланс одного счёта, по одной транзакции на строку.
> Больше информации: <https://hledger.org/hledger.html#aregister>.

- Показать транзакции и текущий баланс счёта `assets:bank:checking`:

`hledger {{[areg|aregister]}} assets:bank:checking`

- Показать транзакции и текущий баланс первого счёта, содержащего `savings` в имени:

`hledger {{[areg|aregister]}} savings`

- Показать подтверждённые транзакции по расчётному счёту с указанной шириной:

`hledger {{[areg|aregister]}} checking {{[-C|--cleared]}} {{[-w|--width]}} {{120}}`

- Показать регистр расчётного счёта, включая транзакции из правил прогнозирования:

`hledger {{[areg|aregister]}} checking --forecast`
