# git-imerge

> Efectuați o îmbinare sau o rebasare între două ramuri Git incremental.
> Conflictele dintre ramuri sunt urmărite până la perechi de angajamente individuale, pentru a simplifica rezolvarea conflictelor.
> Mai multe informaţii: <https://github.com/mhagger/git-imerge>

- Începeți rebase bazate pe imerge (verificați sucursala care urmează să fie rebazată, în primul rând):

`git imerge rebase {{branch_to_rebase_onto}}`

- Începeți îmbinarea bazată pe imerge (verificați sucursala pentru a fuziona în, mai întâi):

`git imerge merge {{branch_to_be_merged}}`

- Arată diagrama ASCII de îmbinare în curs sau rebase:

`git imerge diagram`

- Continua operatiunea imerge dupa rezolvarea conflictelor (`git add` fisierele conflictuale, mai intai):

`git imerge continue --no-edit`

- Înfășurați operațiunea imerge, după ce toate conflictele sunt rezolvate:

`git imerge finish`

- Abandonați operațiunea imerge și reveniți la ramura anterioară:

`git-imerge remove && git checkout {{previous_branch}}`
