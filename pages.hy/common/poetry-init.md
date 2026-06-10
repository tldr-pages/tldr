# պոեզիա նախաձեռնություն

> Ստեղծեք հիմնական `pyproject.toml` ֆայլ ինտերակտիվ կերպով:.
> Լրացուցիչ տեղեկություններ. <https://python-poetry.org/docs/cli/#init>:.

- Ստեղծեք `pyproject.toml` ֆայլ ինտերակտիվ կերպով.:

`poetry init`

- Ստեղծեք `pyproject.toml` ֆայլ՝ նախապես լրացված արժեքներով.:

`poetry init --name {{package_name}} --author "{{author_name <email@example.com>}}"`

- Ստեղծեք `pyproject.toml` ֆայլ առանց փոխազդեցության (օգտագործելով լռելյայն).:

`poetry init {{[-n|--no-interaction]}}`

- Ստեղծեք `pyproject.toml` ֆայլ և ավելացրեք կախվածություն.:

`poetry init --dependency {{package_name}}`

- Ստեղծեք `pyproject.toml` ֆայլ և ավելացրեք զարգացման կախվածություն.:

`poetry init --dev-dependency {{package_name}}`

- Ցուցադրել օգնությունը.:

`poetry init {{[-h|--help]}}`
