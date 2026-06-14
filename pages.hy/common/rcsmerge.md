# rcsmerge

> Միավորել RCS-ի վերանայումները աշխատանքային ֆայլում:.
> Տես նաև՝ `ci`, `co`, `rcs`, `rcsdiff`, `rlog`:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/rcsmerge>:.

- Միավորել երկու վերանայումների միջև եղած տարբերությունները աշխատանքային ֆայլում.:

`rcsmerge -r{{revision1}} -r{{revision2}} {{path/to/file}}`

- Միավորել փոփոխությունները մասնաճյուղի վերանայումից աշխատանքային ֆայլի մեջ.:

`rcsmerge -r{{branch_revision}} {{path/to/file}}`

- Կատարել հանգիստ միաձուլում (ճնշել ախտորոշումը).:

`rcsmerge -q -r{{revision1}} -r{{revision2}} {{path/to/file}}`

- Աշխատանքային ֆայլը վերագրանցելու փոխարեն տպեք արդյունքը `stdout`-ում.:

`rcsmerge -p -r{{revision1}} -r{{revision2}} {{path/to/file}}`
