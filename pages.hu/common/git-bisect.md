# git bisect

> A bináris keresés segítségével megtalálja a hibát bevezető commitot. A Git automatikusan előre-hátra ugrik a commit gráfban, hogy fokozatosan leszűkítse a hibás commitot. További információ: <https://git-scm.com/docs/git-bisect>.

- Indítson bisect munkamenetet egy ismert hibás commit és egy ismert tiszta (jellemzően régebbi) commit által határolt commit tartományon:

`git bisect start {{bad_commit}} {{good_commit}}`

- Minden egyes commitot, amelyet a `git bisect` kiválaszt, jelölje "rossznak" vagy "jónak", miután megvizsgálta a probléma szempontjából:

`git bisect {{good|bad}}`

- Miután a `git bisect` azonosította a hibás commitot, fejezze be a bisect munkamenetet, és térjen vissza az előző ághoz:

`git bisect reset`

- Hagyjon ki egy commitot a bisect során (pl. olyat, amelyik egy másik probléma miatt megbukik a teszteken):

`git bisect skip`

- Naplót jeleníthet meg az eddig elvégzett munkákról:

`git bisect log`
