# git cherry-pick

> A meglévő commitok által bevezetett változtatások alkalmazása az aktuális ágra. Ha a változtatásokat egy másik ágra szeretné alkalmazni, először a `git checkout` segítségével váltson a kívánt ágra. További információ: <https://git-scm.com/docs/git-cherry-pick>.

- Alkalmazzon egy commitot az aktuális ágra:

`git cherry-pick {{commit}}`

- Commitek egy sorának alkalmazása az aktuális ágra (lásd még: `git rebase --onto`):

`git cherry-pick {{start_commit}}~..{{end_commit}}`

- Több (nem egymást követő) commit alkalmazása az aktuális ágra:

`git cherry-pick {{commit_1}} {{commit_2}}`

- Egy commit módosításainak hozzáadása a munkakönyvtárhoz, commit létrehozása nélkül:

`git cherry-pick -n {{commit}}`
