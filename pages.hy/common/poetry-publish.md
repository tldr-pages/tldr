# պոեզիա հրատարակել

> Հրապարակեք փաթեթը հեռավոր պահեստում:.
> Լրացուցիչ տեղեկություններ. <https://python-poetry.org/docs/cli/#publish>:.

- Հրապարակեք ընթացիկ փաթեթը PyPI-ում.:

`poetry publish`

- Կառուցեք փաթեթը հրապարակելուց առաջ.:

`poetry publish --build`

- Հրապարակել կոնկրետ պահեստում.:

`poetry publish {{[-r|--repository]}} {{repository_name}}`

- Հրապարակեք հատուկ հավատարմագրերով.:

`poetry publish {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}}`

- Կատարեք չոր վազք՝ տեսնելու, թե ինչ է արվելու առանց իրականում հրապարակելու.:

`poetry publish --dry-run`

- Բաց թողնել ֆայլերը, որոնք արդեն գոյություն ունեն պահոցում.:

`poetry publish --skip-existing`
