# ուլտրամանուշակագույն վազք

> Գործարկեք հրաման կամ սցենար ծրագրի միջավայրում:.
> Լրացուցիչ տեղեկություններ. <https://docs.astral.sh/uv/reference/cli/#uv-run>:.

- Գործարկել Python սցենար.:

`uv run {{path/to/script.py}}`

- Գործարկել Python մոդուլը.:

`uv run {{[-m|--module]}} {{module_name}}`

- Գործարկեք հրաման՝ ժամանակավորապես տեղադրված լրացուցիչ փաթեթներով.:

`uv run {{[-w|--with]}} {{package}} {{command}}`

- Գործարկեք սցենար պահանջների ֆայլից փաթեթներով.:

`uv run --with-requirements {{path/to/requirements.txt}} {{path/to/script.py}}`

- Գործարկել մեկուսացված միջավայրում (առանց նախագծի կախվածության).:

`uv run --isolated {{path/to/script.py}}`

- Գործարկեք առանց միջավայրի համաժամացման նախ.:

`uv run --no-sync {{command}}`
