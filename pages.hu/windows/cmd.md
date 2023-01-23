# cmd

> A Windows parancsértelmezője. További információ: <https://learn.microsoft.com/windows-server/administration/windows-commands/cmd>.

- Interaktív shell munkamenet indítása:

`cmd`

- Egy \[c\]ommand végrehajtása:

`cmd /c "{{command}}"`

- Szkript végrehajtása:

`cmd {{path/to/file.bat}}`

- Parancs végrehajtása, majd interaktív héjba lépés:

`cmd /k "{{command}}"`

- Interaktív héj munkamenet indítása, ahol a `echo` a parancsok kimeneténél ki van kapcsolva:

`cmd /q`

- Interaktív shell munkamenet indítása késleltetett \[v\]ariable bővítés engedélyezésével vagy letiltásával:

`cmd /v:{{on|off}}`

- Interaktív shell munkamenet indítása a parancs \[e\]xtensions engedélyezésével vagy letiltásával:

`cmd /e:{{on|off}}`

- Interaktív shell munkamenet indítása használt Unicode kódolással:

`cmd /u`
