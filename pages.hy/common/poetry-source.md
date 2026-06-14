# պոեզիայի աղբյուր

> Ավելացրեք աղբյուրի կոնֆիգուրացիաներ ձեր Poetry նախագծին:.
> Տես նաև՝ `asdf`:.
> Լրացուցիչ տեղեկություններ. <https://python-poetry.org/docs/cli/#source>:.

- Ավելացնել աղբյուրի կոնֆիգուրացիա.:

`poetry source add {{source_name}} {{source_url}}`

- Սահմանեք աղբյուրի առաջնահերթությունը.:

`poetry source add --priority {{primary|supplemental|explicit}} {{source_name}} {{source_url}}`

- Ցուցադրել տեղեկատվություն բոլոր աղբյուրների համար.:

`poetry source show`

- Ցուցադրել տեղեկատվություն կոնկրետ աղբյուրի համար.:

`poetry source show {{source_name}}`

- Հեռացրեք աղբյուրը ձեր `pyproject.toml` ֆայլից.:

`poetry source remove {{source_name}}`
