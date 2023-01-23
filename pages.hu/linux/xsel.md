# xsel

> X11 kijelölő és vágólapkezelő eszköz. További információ: <https://manned.org/xsel>.

- Egy parancs kimenete a clip\[b\]oard bemeneteként való használata (egyenértékű a `Ctrl + C`):

`echo 123 | xsel -ib`

- Egy fájl tartalmának használata a vágólap bemeneteként:

`cat {{path/to/file}} | xsel -ib`

- A vágólap tartalmának kimenete a terminálba (egyenértékű a `Ctrl + V`):

`xsel -ob`

- A vágólap tartalmának kiadása egy fájlba:

`xsel -ob > {{path/to/file}}`

- A vágólap törlése:

`xsel -cb`

- Az X11 elsődleges kijelölés tartalmának kimenete a terminálba (az egér középső kattintásával egyenértékű):

`xsel -op`
