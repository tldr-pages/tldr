# at

> Parancsok végrehajtása egy megadott időpontban. További információ: <https://man.archlinux.org/man/at.1>.

- Nyisson meg egy `at` promptot új ütemezett parancsok létrehozásához, majd a mentéshez és kilépéshez nyomja meg a `Ctrl + D` gombot:

`at {{hh:mm}}`

- A parancsok végrehajtása és az eredmény elküldése e-mailben egy helyi levelezőprogrammal, például a Sendmail segítségével:

`at {{hh:mm}} -m`

- Egy parancsfájl végrehajtása a megadott időpontban:

`at {{hh:mm}} -f {{path/to/file}}`

- Rendszeres értesítés megjelenítése február 18-án 23 órakor:

`echo "notify-send '{{Wake up!}}'" | at {{11pm}} {{Feb 18}}`
