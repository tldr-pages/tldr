# qtile

> Egy Python nyelven írt és konfigurált, teljes funkcionalitású, hackelhető csempéző ablakkezelő. További információ: <https://docs.qtile.org/en/latest/manual/commands/shell/index.html>.

- Indítsd el az ablakkezelőt, ha még nem fut (ideális esetben a `.xsession` vagy hasonló oldalról kell futtatni):

`qtile start`

- Ellenőrizze a konfigurációs fájlban a fordítási hibákat (alapértelmezett hely: `~/.config/qtile/config.py`):

`qtile check`

- Jelenlegi erőforrás-felhasználási információk megjelenítése:

`qtile top --force`

- Nyissa meg a `xterm` programot lebegő ablakként a `test-group` nevű csoporton:

`qtile run-cmd --group {{test-group}} --float {{xterm}}`

- Indítsa újra az ablakkezelőt:

`qtile cmd-obj --object cmd --function restart`
