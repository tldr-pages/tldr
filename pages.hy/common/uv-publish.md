# uv հրապարակում

> Վերբեռնեք բաշխումները ինդեքսում:.
> Լրացուցիչ տեղեկություններ. <https://docs.astral.sh/uv/reference/cli/#uv-publish>:.

- Փաթեթներ հրապարակեք `dist/` գրացուցակից (կանխադրված վարքագիծ).:

`uv publish`

- Հրապարակեք հատուկ պահեստի URL.:

`uv publish --publish-url {{https://upload.pypi.org/legacy/}}`

- Հրապարակել՝ օգտագործելով հատուկ օգտանուն և գաղտնաբառ.:

`uv publish {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}}`

- Հրապարակեք API նշանի միջոցով.:

`uv publish {{[-t|--token]}} {{your_api_token}}`

- Հրապարակեք հատուկ բաշխման ֆայլեր.:

`uv publish {{path/to/dist/*.whl}} {{path/to/dist/*.tar.gz}}`

- Փորձարկման համար հրապարակեք TestPyPI-ում.:

`uv publish --publish-url https://test.pypi.org/legacy/`
