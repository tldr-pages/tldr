# git name-rev

> Նկարագրեք commit-ը` օգտագործելով գոյություն ունեցող ref անունները:.
> Լրացուցիչ տեղեկություններ. <https://git-scm.com/docs/git-name-rev>:.

- Ցույց տալ `HEAD` անունը՝:

`git name-rev HEAD`

- Ցույց տալ միայն անունը.:

`git name-rev --name-only HEAD`

- Թվարկեք բոլոր համապատասխանող անունները.:

`git name-rev --all`

- Օգտագործեք միայն պիտակներ՝ պարտավորությունը անվանելու համար.:

`git name-rev --tags HEAD`

- Անհայտ պարտավորությունների համար `undefined` տպելու փոխարեն դուրս եկեք ոչ զրոյական կարգավիճակի կոդով.:

`git name-rev --no-undefined {{commit-ish}}`

- Ցույց տալ անունները բազմաթիվ պարտավորությունների համար.:

`git name-rev HEAD~1 HEAD~2 main`

- Սահմանափակել անունները ճյուղերի հղումներով.:

`git name-rev --refs refs/heads/ {{commit-ish}}`

- Կարդացեք պարտավորությունների ID-ները `stdin`-ից՝:

`echo "{{commit-ish}}" | git name-rev --annotate-stdin`
