# gh գաղտնի հավաքածու

> Ստեղծեք կամ թարմացրեք GitHub գաղտնիքները:.
> Լրացուցիչ տեղեկություններ. <https://cli.github.com/manual/gh_secret_set>:.

- Սահմանեք գաղտնիք ընթացիկ պահոցի համար (օգտագործողին կառաջարկվի արժեքը).:

`gh secret set {{name}}`

- Սահմանեք գաղտնիք ֆայլից ընթացիկ պահոցի համար.:

`gh < {{path/to/file}} secret set {{name}}`

- Սահմանեք գաղտնիք կոնկրետ պահեստի համար.:

`gh secret set {{name}} {{[-b|--body]}} {{value}} {{[-R|--repo]}} {{owner}}/{{repository}}`

- Սահմանեք կազմակերպության գաղտնիք հատուկ պահոցների համար.:

`gh secret set {{name}} {{[-o|--org]}} {{organization}} {{[-r|--repos]}} "{{repository1,repository2,...}}"`

- Սահմանեք կազմակերպության գաղտնիքը հատուկ տեսանելիությամբ.:

`gh secret set {{name}} {{[-o|--org]}} {{organization}} {{[-v|--visibility]}} {{all|private|selected}}`
