# gh ռեպո ստեղծել

> Ստեղծեք նոր GitHub պահոց:.
> Նշում․ `--public`, `--private` կամ `--internal` պահանջվում է, երբ ինտերակտիվորեն չի աշխատում:.
> Լրացուցիչ տեղեկություններ. <https://cli.github.com/manual/gh_repo_create>:.

- Ստեղծեք նոր պահեստ ինտերակտիվ կերպով.:

`gh repo {{[new|create]}}`

- Ստեղծեք անձնական պահոց ընթացիկ գրացուցակից.:

`gh repo {{[new|create]}} {{[-s|--source]}} . --private`

- Ստեղծեք հանրային պահոց ընթացիկ գրացուցակից.:

`gh repo {{[new|create]}} {{[-s|--source]}} . --public`

- Ստեղծեք հանրային պահեստ՝ նշված անունով և նկարագրությամբ.:

`gh repo {{[new|create]}} {{repo_name}} {{[-d|--description]}} "{{repo_description}}" --public`

- Ստեղծումից հետո կլոնավորեք նոր պահոցը տեղում.:

`gh repo {{[new|create]}} {{repo_name}} {{[-c|--clone]}} {{--public|--private|--internal}}`
