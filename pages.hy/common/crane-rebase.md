# Վերամբարձ կռունկ

> Վերափոխեք պատկերը նոր բազային պատկերի վրա:.
> Լրացուցիչ տեղեկություններ. <https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane_rebase.md>:.

- Վերափոխել պատկերը:

`crane rebase`

- Տեղադրելու համար նոր բազային պատկեր.:

`crane rebase --new_base {{image_name}}`

- Հին բազային պատկերը հեռացնելու համար.:

`crane rebase --old_base {{image_name}}`

- Վերաբացված պատկերին կիրառելու համար հատկորոշեք.:

`crane rebase {{[-t|--tag]}} {{tag_name}}`

- Ցուցադրել օգնությունը.:

`crane rebase {{[-h|--help]}}`
