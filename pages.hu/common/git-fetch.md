# git fetch

> Objektumok és hivatkozások letöltése egy távoli tárolóból. További információ: <https://git-scm.com/docs/git-fetch>.

- A legfrissebb módosítások lekérése az alapértelmezett távoli upstream tárolóból (ha be van állítva):

`git fetch`

- Új ágak lekérése egy adott távoli upstream tárolóból:

`git fetch {{remote_name}}`

- A legfrissebb módosítások lekérése az összes távoli upstream tárolóból:

`git fetch --all`

- Címkék lekérése a távoli upstream tárolóból is:

`git fetch --tags`

- Törli a távoli ágakra való helyi hivatkozásokat, amelyek upstream módon törlődtek:

`git fetch --prune`
