# ք

> Կատարեք SQL-ի նման հարցումներ CSV և TSV ֆայլերի վրա:.
> Լրացուցիչ տեղեկություններ. <https://harelba.github.io/q/>:.

- Հարցրեք CSV ֆայլ՝ սահմանազատիչը նշելով որպես ',':

`q {{[-d|--delimiter]}} ',' "SELECT * from {{path/to/file}}"`

- Հարցրեք TSV ֆայլ.:

`q {{[-t|--tab-delimited]}} "SELECT * from {{path/to/file}}"`

- Հարցման ֆայլ վերնագրի տողով.:

`q {{[-d|--delimiter]}} {{delimiter}} {{[-H|--skip-header]}} "SELECT * from {{path/to/file}}"`

- Կարդացեք տվյալները `stdin`-ից; «-»-ը հարցումում ներկայացնում է տվյալներ `stdin`-ից՝:

`{{output}} | q "select * from -"`

- Միացրեք երկու ֆայլ (օրինակ՝ `f1` և `f2` օրինակում) `c1` սյունակում, ընդհանուր սյունակ.:

`q "SELECT * FROM {{path/to/file}} f1 JOIN {{path/to/other_file}} f2 ON (f1.c1 = f2.c1)"`

- Ձևաչափեք ելքը՝ օգտագործելով ելքային սահմանազատիչ՝ ելքային վերնագրի տողով (Ծանոթագրություն. Command-ը կթողարկի սյունակների անվանումները՝ հիմնված մուտքային ֆայլի վերնագրի կամ հարցումում չեղարկված սյունակների անունների վրա).:

`q {{[-D|--output-delimiter]}} {{delimiter}} {{[-O|--output-header]}} "SELECT {{column}} as {{alias}} from {{path/to/file}}"`
