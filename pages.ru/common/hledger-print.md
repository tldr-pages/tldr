# hledger print

> Показывать полные записи журнала, представляющие транзакции.
> Больше информации: <https://hledger.org/hledger.html#print>.

- Показать все транзакции в файле журнала по умолчанию:

`hledger print`

- Показать транзакции, раскрыв все подразумеваемые суммы или стоимости:

`hledger print {{[-x|--explicit]}} --infer-costs`

- Показать транзакции из двух указанных файлов с суммами, конвертированными в стоимость:

`hledger print {{[-f|--file]}} {{путь/к/2023.journal}} {{[-f|--file]}} {{путь/к/2024.journal}} {{[-B|--cost]}}`

- Показать транзакции в `$` за текущий месяц по счетам, содержащим `food`, но не `groceries`:

`hledger print cur:\\$ food not:groceries date:thismonth`

- Показать транзакции на сумму 50 или более с `whole foods` в описании:

`hledger print amt:'>50' desc:'whole foods'`

- Показать подтверждённые транзакции с суммами в `EUR`, округлёнными и с десятичными запятыми:

`hledger print {{[-C|--cleared]}} --commodity '1000, EUR' --round hard`

- Записать транзакции из `foo.journal` в CSV-файл:

`hledger print {{[-f|--file]}} {{путь/к/foo.journal}} {{[-o|--output-file]}} {{путь/к/выходному_файлу.csv}}`
