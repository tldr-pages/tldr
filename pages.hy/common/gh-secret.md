# gh գաղտնիք

> Կառավարեք GitHub գաղտնիքները:.
> Լրացուցիչ տեղեկություններ. <https://cli.github.com/manual/gh_secret>:.

- Թվարկեք ընթացիկ պահոցի գաղտնի բանալիները.:

`gh secret {{[ls|list]}}`

- Թվարկեք գաղտնի բանալիները որոշակի կազմակերպության համար.:

`gh secret {{[ls|list]}} {{[-o|--org]}} {{organization}}`

- Թվարկեք գաղտնի բանալիները որոշակի պահոցի համար.:

`gh secret {{[ls|list]}} {{[-R|--repo]}} {{owner}}/{{repository}}`

- Սահմանեք գաղտնիք ընթացիկ պահոցի համար (օգտագործողին կառաջարկվի արժեքը).:

`gh secret set {{name}}`

- Սահմանեք գաղտնիք ֆայլից ընթացիկ պահոցի համար.:

`gh < {{path/to/file}} secret set {{name}}`

- Սահմանեք կազմակերպության գաղտնիք հատուկ պահոցների համար.:

`gh secret set {{name}} {{[-o|--org]}} {{organization}} {{[-r|--repos]}} {{repository1,repository2}}`

- Հեռացրեք գաղտնիքը ընթացիկ պահոցի համար.:

`gh secret remove {{name}}`

- Հեռացնել գաղտնիքը կոնկրետ կազմակերպության համար.:

`gh secret remove {{name}} {{[-o|--org]}} {{organization}}`
