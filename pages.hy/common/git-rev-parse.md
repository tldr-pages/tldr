# git rev-վերլուծել

> Ցուցադրել վերանայումների հետ կապված մետատվյալները:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-rev-parse>:.

- Ստացեք մասնաճյուղի commit hash-ը.:

`git rev-parse {{branch_name}}`

- Ստացեք ընթացիկ մասնաճյուղի անունը.:

`git rev-parse --abbrev-ref {{HEAD}}`

- Ստացեք բացարձակ ուղին դեպի արմատային գրացուցակ.:

`git rev-parse --show-toplevel`
