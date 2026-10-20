# hledger incomestatement

> Показывать поступления доходов и оттоки расходов за отчётный период.
> Суммы отображаются с обычным положительным знаком, как в стандартной финансовой отчётности.
> Больше информации: <https://hledger.org/hledger.html#incomestatement>.

- Показать доходы и расходы (изменения по счетам `Revenue` и `Expense`):

`hledger {{[is|incomestatement]}}`

- Показать доходы и расходы помесячно:

`hledger {{[is|incomestatement]}} {{[-M|--monthly]}}`

- Показать ежемесячные доходы/расходы/итоги, по убыванию, с группировкой до 2-го уровня:

`hledger {{[is|incomestatement]}} {{[-MTAS|--monthly --row-total --average --sort-amount]}} {{[-2|--depth 2]}}`

- Показать ежемесячные доходы/расходы/итоги с группировкой до 2-го уровня и сохранить в HTML-файл `is.html`:

`hledger {{[is|incomestatement]}} {{[-MTAS|--monthly --row-total --average --sort-amount]}} {{[-2|--depth 2]}} {{[-o|--output-file]}} is.html`
