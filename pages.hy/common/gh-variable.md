# gh փոփոխական

> Կառավարեք GitHub գործողությունները և Dependabot փոփոխականները:.
> Լրացուցիչ տեղեկություններ. <https://cli.github.com/manual/gh_variable>:.

- Ցուցակեք փոփոխականները ընթացիկ պահոցի համար.:

`gh variable {{[ls|list]}}`

- Նշեք փոփոխականները որոշակի կազմակերպության համար.:

`gh variable {{[ls|list]}} {{[-o|--org]}} {{organization}}`

- Ստացեք փոփոխական ընթացիկ պահոցի համար.:

`gh variable get {{name}}`

- Սահմանեք փոփոխական ընթացիկ պահոցի համար (օգտագործողին կառաջարկվի արժեքը).:

`gh variable set {{name}}`

- Ներկայիս պահոցում տեղակայման միջավայրի համար փոփոխական սահմանեք.:

`gh variable set {{name}} {{[-e|--env]}} {{environment_name}}`

- Սահմանեք կազմակերպության փոփոխական, որը տեսանելի է բոլոր պահեստների համար.:

`gh variable set {{name}} {{[-o|--org]}} {{organization}} {{[-v|--visibility]}} all`

- Սահմանեք մի քանի փոփոխականներ dotenv ֆայլից.:

`gh variable set {{[-f|--env-file]}} {{path/to/file.env}}`

- Ջնջել փոփոխականը ընթացիկ պահոցի համար.:

`gh variable delete {{name}}`
