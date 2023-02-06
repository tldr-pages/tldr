# git rebase

> Az egyik ág commitjainak újbóli alkalmazása egy másik ágon. Általában egy teljes ág "áthelyezésére" használják egy másik bázisra, létrehozva a commitok másolatait az új helyen. További információ: <https://git-scm.com/docs/git-rebase>.

- Az aktuális ág újraalapozása egy másik megadott ág tetejére:

`git rebase {{new_base_branch}}`

- Interaktív rebase indítása, amely lehetővé teszi a commitok átrendezését, elhagyását, kombinálását vagy módosítását:

`git rebase -i {{target_base_branch_or_commit_hash}}`

- Folytathatja az egyesítési hiba miatt megszakadt újraalapozást, miután szerkesztette az ütköző fájlokat:

`git rebase --continue`

- Folytathatja az egyesítési konfliktusok miatt szüneteltetett újraindítást az ütköző commit kihagyásával:

`git rebase --skip`

- Folyamatban lévő újraalapozás megszakítása (pl. ha azt összeolvasztási konfliktus szakítja meg):

`git rebase --abort`

- Az aktuális ág egy részének áthelyezése egy új bázisra, a régi bázis megadásával:

`git rebase --onto {{new_base}} {{old_base}}`

- Az utolsó 5 commit helyben történő újbóli alkalmazása, megállva, hogy lehetővé tegye azok újrarendezését, elhagyását, kombinálását vagy módosítását:

`git rebase -i {{HEAD~5}}`

- Automatikusan oldja fel az esetleges konfliktusokat a működő ág verziójának előnyben részesítésével (`theirs` kulcsszó ebben az esetben fordított jelentéssel bír):

`git rebase -X theirs {{branch_name}}`
