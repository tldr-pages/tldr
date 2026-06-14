# ուլտրամանուշակագույն հեռացում

> Հեռացրեք կախվածությունները նախագծի `pyproject.toml` ֆայլից:.
> Լրացուցիչ տեղեկություններ. <https://docs.astral.sh/uv/reference/cli/#uv-remove>:.

- Հեռացրեք կախվածությունը նախագծից.:

`uv remove {{package}}`

- Հեռացրեք բազմաթիվ կախվածությունները.:

`uv remove {{package1 package2 ...}}`

- Հեռացնել զարգացման կախվածությունը.:

`uv remove --dev {{package}}`

- Հեռացրեք կախվածությունը կամընտիր կախվածության խմբից.:

`uv remove --optional {{extra_name}} {{package}}`

- Հեռացրեք կախվածությունը որոշակի կախվածության խմբից.:

`uv remove --group {{group_name}} {{package}}`

- Հեռացրեք առանց վիրտուալ միջավայրի համաժամացման.:

`uv remove --no-sync {{package}}`
