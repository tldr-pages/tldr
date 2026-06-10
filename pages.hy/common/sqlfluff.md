# sqlfluff

> Lint և ավտոմատ ձևաչափեք SQL ֆայլերը բազմաթիվ բարբառներով:.
> Լրացուցիչ տեղեկություններ. <https://docs.sqlfluff.com/en/stable/reference/cli.html>:.

- Տեղադրեք SQL ֆայլը կամ գրացուցակը որոշակի բարբառով.:

`sqlfluff lint {{[-d|--dialect]}} {{dialect}} {{path/to/file_or_directory}}`

- Ավտոմատ ձևաչափեք SQL ֆայլը կամ գրացուցակը որոշակի բարբառով.:

`sqlfluff format {{[-d|--dialect]}} {{dialect}} {{path/to/file_or_directory}}`

- Ավտոմատ կերպով շտկել linting խախտումները SQL ֆայլում կամ գրացուցակում.:

`sqlfluff fix {{[-d|--dialect]}} {{dialect}} {{[-r|--rules]}} {{rule1,rule2,...}} {{path/to/file_or_directory}}`

- Վերլուծեք SQL ֆայլը կամ գրացուցակը և ցուցադրեք վերլուծության ծառը.:

`sqlfluff parse {{[-d|--dialect]}} {{dialect}} {{path/to/file_or_directory}}`

- Ցույց տալ բոլոր աջակցվող SQL բարբառները.:

`sqlfluff dialects`
