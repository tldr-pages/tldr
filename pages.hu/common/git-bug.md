# git bug

> Egy elosztott hibakövető, amely a git belső tárolóját használja, így nem kerülnek fájlok a projektedbe. A problémáidat ugyanarra a git távolira küldheted be, amelyet másokkal való interakcióra használsz, hasonlóan a commitokhoz és ágakhoz. További információ: <https://github.com/MichaelMure/git-bug/blob/master/doc/md/git-bug.md>.

- Új identitás létrehozása:

`git bug user create`

- Új hiba létrehozása:

`git bug add`

- Az új bejegyzést egy távolira tolhatja:

`git bug push`

- Frissítéseket húzhatsz ki (pull):

`git bug pull`

- Lista a meglévő hibákról:

`git bug ls`

- A hibák szűrése és rendezése lekérdezéssel:

`git bug ls "{{status}}:{{open}} {{sort}}:{{edit}}"`

- Hibák keresése szöveges tartalom alapján:

`git bug ls "{{search_query}}" baz`
