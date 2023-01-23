# git mailinfo

> A javítási és szerzői információk kivonása egyetlen e-mail üzenetből. További információ: <https://git-scm.com/docs/git-mailinfo>.

- A javítási és szerzői adatok kivonása egy e-mail üzenetből:

`git mailinfo {{message|patch}}`

- Kivonja, de eltávolítja a vezető és az utolsó szóközöket:

`git mailinfo -k {{message|patch}}`

- Távolítson el mindent a szövegtestből az ollós sor előtt (pl. "-->\* --"), és nyerje ki az üzenetet vagy a javítást:

`git mailinfo --scissors {{message|patch}}`
