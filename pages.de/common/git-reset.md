# git reset

> Mache Commits rückgängig oder unstage Änderungen, indem du den aktuellen Git HEAD auf den angegebenen Zustand zurücksetzt.
> Wenn ein Pfad übergeben wird, funktioniert es als "unstage"; wenn ein Commit-Hash oder ein Branch übergeben wird, funktioniert es als "uncommit".
> Weitere Informationen: <https://git-scm.com/docs/git-reset>.

- Unstage alles:

`git reset`

- Unstage bestimmte Datei(en):

`git reset {{pfad/zu/datei1 pfad/zu/datei2 ...}}`

- Unstage interaktiv Teile einer Datei:

`git reset {{[-p|--patch]}} {{pfad/zu/datei}}`

- Mache den letzten Commit rückgängig, behalte dessen Änderungen (und alle weiteren nicht committeten Änderungen) im Dateisystem:

`git reset HEAD~`

- Mache die letzten beiden Commits rückgängig, füge deren Änderungen dem Index hinzu, d.h. zum Commit gestaged:

`git reset --soft HEAD~2`

- Verwirf alle nicht committeten Änderungen, ob gestaged oder nicht (für nur nicht gestagte Änderungen verwende bitte `git checkout`):

`git reset --hard`

- Setze das Repository auf einen bestimmten Commit zurück, verwirfe seitdem committete, gestagte und nicht gestagte Änderungen:

`git reset --hard {{commit}}`
