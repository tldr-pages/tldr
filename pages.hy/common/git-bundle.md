# git փաթեթ

> Փաթեթավորեք առարկաները և հղումները արխիվում:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-bundle>:.

- Ստեղծեք փաթեթային ֆայլ, որը պարունակում է որոշակի ճյուղի բոլոր օբյեկտները և հղումները.:

`git bundle create {{path/to/file.bundle}} {{branch_name}}`

- Ստեղծեք բոլոր ճյուղերի փաթեթային ֆայլ.:

`git bundle create {{path/to/file.bundle}} --all`

- Ստեղծեք ընթացիկ ճյուղի վերջին 5 պարտավորությունների փաթեթային ֆայլ.:

`git bundle create {{path/to/file.bundle}} -5 {{HEAD}}`

- Ստեղծեք վերջին 7 օրվա փաթեթային ֆայլ.:

`git bundle create {{path/to/file.bundle}} --since 7.days {{HEAD}}`

- Ստուգեք, որ փաթեթի ֆայլը վավեր է և կարող է կիրառվել ընթացիկ պահոցում.:

`git bundle verify {{path/to/file.bundle}}`

- Տպեք `stdout` փաթեթում պարունակվող հղումների ցանկը՝:

`git bundle unbundle {{path/to/file.bundle}}`

- Փաթեթային ֆայլից առանձնացնել որոշակի ճյուղ ընթացիկ պահոց.:

`git pull {{path/to/file.bundle}} {{branch_name}}`

- Ստեղծեք նոր պահոց փաթեթից.:

`git clone {{path/to/file.bundle}}`
