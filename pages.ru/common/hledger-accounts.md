# hledger accounts

> Выводить список имён счетов.
> Больше информации: <https://hledger.org/hledger.html#accounts>.

- Показать все счета, использованные или объявленные в файле журнала по умолчанию:

`hledger {{[acc|accounts]}}`

- Показать счета, использованные в транзакциях:

`hledger {{[acc|accounts]}} {{[-u|--used]}}`

- Показать счета, объявленные с помощью директив account:

`hledger {{[acc|accounts]}} {{[-d|--declared]}}`

- Добавить новые директивы account для использованных, но не объявленных счетов в журнал:

`hledger {{[acc|accounts]}} --undeclared --directives >> {{2024-accounts.journal}}`

- Показать счета, содержащие `asset` в имени, и их объявленные/выведенные типы:

`hledger {{[acc|accounts]}} asset --types`

- Показать счета типа `Asset`:

`hledger {{[acc|accounts]}} type:A`

- Показать первые два уровня иерархии счетов:

`hledger {{[acc|accounts]}} {{[-t|--tree]}} {{[-2|--depth 2]}}`
