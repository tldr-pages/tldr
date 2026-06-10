# ուլտրամանուշակագույն սկիզբ

> Ստեղծեք նոր Python նախագիծ:.
> Լրացուցիչ տեղեկություններ. <https://docs.astral.sh/uv/reference/cli/#uv-init>:.

- Նախաձեռնեք նախագիծը ընթացիկ գրացուցակում.:

`uv init`

- Նախաձեռնեք որոշակի անունով նախագիծ.:

`uv init {{project_name}}`

- Ստեղծեք նախագիծ տվյալ գրացուցակում.:

`uv init --directory {{path/to/directory}} {{project_name}}`

- Ստեղծեք նախագիծ Python գրադարանի համար.:

`uv init {{[--lib|--library]}} {{project_name}}`

- Նշեք կառուցման համակարգը.:

`uv init --build-backend {{build_backend}} {{project_name}}`

- Ստեղծեք միայն `pyproject.toml`:

`uv init --bare {{project_name}}`

- Սահմանեք նախագծի նկարագրությունը.:

`uv init --description "{{description}}" {{project_name}}`
