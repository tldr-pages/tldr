# aws կազմաձևում

> Կառավարեք AWS CLI-ի կոնֆիգուրացիան:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/configure/>:.

- Կազմաձևեք AWS CLI-ն ինտերակտիվորեն (ստեղծում է նոր կազմաձև կամ թարմացնում է լռելյայն).:

`aws configure`

- AWS CLI-ի համար ինտերակտիվ կերպով կազմաձևեք անվանված պրոֆիլը (ստեղծում է նոր պրոֆիլ կամ թարմացնում գոյություն ունեցողը).:

`aws configure --profile {{profile_name}}`

- Ցուցադրել արժեքը որոշակի կազմաձևման փոփոխականից.:

`aws configure get {{name}}`

- Ցուցադրել որոշակի պրոֆիլում կազմաձևման փոփոխականի արժեքը.:

`aws configure get {{name}} --profile {{profile_name}}`

- Սահմանեք որոշակի կազմաձևման փոփոխականի արժեքը.:

`aws configure set {{name}} {{value}}`

- Սահմանեք կազմաձևման փոփոխականի արժեքը որոշակի պրոֆիլում.:

`aws configure set {{name}} {{value}} --profile {{profile_name}}`

- Թվարկեք կազմաձևման գրառումները.:

`aws configure list`

- Թվարկեք կոնֆիգուրացիայի գրառումները որոշակի պրոֆիլի համար.:

`aws configure list --profile {{profile_name}}`
