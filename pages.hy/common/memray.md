# memray

> Python հավելվածի պրոֆիլի հիշողության օգտագործումը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/bloomberg/memray#usage>:.

- Գործարկել Python ֆայլը և հետևել հիշողության օգտագործմանը.:

`memray run {{path/to/file}}.py`

- Գործարկեք [m] մոդուլ և հետևեք հիշողության օգտագործմանը.:

`memray run -m {{module_name}}`

- Նշեք ելքային անունը.:

`memray run {{[-o|--output]}} {{path/to/output_file}}.bin {{path/to/file}}.py`

- Ցուցադրել հիշողության օգտագործման ամփոփ նկարագիրը.:

`memray summary {{path/to/file}}.bin`

- Ստեղծեք HTML ֆլեյմգրաֆ.:

`memray flamegraph {{path/to/file}}.bin`
