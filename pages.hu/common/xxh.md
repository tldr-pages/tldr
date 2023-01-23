# xxh

> Hozd el a héjadat az összes testreszabásoddal együtt SSH munkameneteken keresztül. Megjegyzés: Az xxh nem telepít semmit a célgép rendszerkönyvtáraiba; a `~/.xxh` eltávolítása az xxh minden nyomát törli a célgépen. További információ: <https://github.com/xxh/xxh>.

- Csatlakozzon egy állomáshoz, és futtassa az aktuális shell-t:

`xxh "{{host}}"`

- Az aktuális shell telepítése a célgépre kérés nélkül:

`xxh "{{host}}" ++install`

- A megadott shell futtatása a célgépen:

`xxh "{{host}}" ++shell {{xonsh|zsh|fish|bash|osquery}}`

- Egy adott xxh konfigurációs könyvtár használata a célgépen:

`xxh "{{host}}" ++host-xxh-home {{~/.xxh}}`

- A megadott konfigurációs fájl használata a gazdaszámítógépen:

`xxh "{{host}}" ++xxh-config {{~/.config/xxh/config.xxhc}}`

- Az SSH-kapcsolathoz használandó jelszó megadása:

`xxh "{{host}}" ++password "{{password}}"`

- Egy xxh csomag telepítése a célgépre:

`xxh "{{host}}" ++install-xxh-packages {{package}}`

- Környezeti változó beállítása a célgépen a shell folyamathoz:

`xxh "{{host}}" ++env {{name}}={{value}}`
