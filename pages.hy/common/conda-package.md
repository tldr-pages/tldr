# կոնդա փաթեթ

> Ստեղծեք ցածր մակարդակի կոնդա փաթեթներ:.
> Լրացուցիչ տեղեկություններ. <https://docs.conda.io/projects/conda/en/stable/commands/package.html>:.

- Ստացեք conda փաթեթը ֆայլից.:

`conda package {{[-w|--which]}} {{path/to/file}}`

- Հեռացրեք բոլոր չհետևված ֆայլերը.:

`conda package {{[-r|--reset]}}`

- Ցուցադրել բոլոր չհետևված ֆայլերը.:

`conda package {{[-u|--untracked]}}`

- Նշեք ստեղծվող փաթեթի փաթեթի անվանումը.:

`conda package --pkg-name {{name}}`

- Նշանակել ստեղծվող փաթեթի փաթեթային տարբերակը.:

`conda package --pkg-version {{version}}`

- Նշեք ստեղծվող փաթեթի փաթեթի կառուցման համարը.:

`conda package --pkg-build {{build_number}}`
