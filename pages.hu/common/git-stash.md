# git stash

> A helyi Git módosítások tárolása egy ideiglenes területen. További információ: <https://git-scm.com/docs/git-stash>.

- Az aktuális változtatások tárolása, kivéve az új (nem követett) fájlokat:

`git stash push -m {{optional_stash_message}}`

- Stash current changes, including new (untracked) files:

`git stash -u`

- Interaktívan kiválaszthatja a módosított fájlok részeit a tároláshoz:

`git stash -p`

- Az összes elrejtés listázása (megjeleníti az összes elrejtés nevét, a kapcsolódó ágat és az üzenetet):

`git stash list`

- A változtatások megjelenítése javításként a stash (alapértelmezett a stash@{0}) és a stash-bejegyzés létrehozásakor visszamenő commit között:

`git stash show -p {{stash@{0}}}`

- Alkalmazza a stash-t (alapértelmezett a legújabb, neve stash@{0}):

`git stash apply {{optional_stash_name_or_commit}}`

- Eldobni vagy alkalmazni egy stash-t (alapértelmezett a stash@{0}), és eltávolítani a stash-listáról, ha az alkalmazás nem okoz konfliktust:

`git stash pop {{optional_stash_name}}`

- Dobja el az összes stash-t:

`git stash clear`
