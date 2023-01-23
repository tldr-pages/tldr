# wal-telegram

> A pywal/wal által generált színek alapján témákat generál a Telegram számára. További információ: <https://github.com/guillaumeboehm/wal-telegram>.

- Generálás a wal palettájával és az aktuális háttérképekkel (csak feh):

`wal-telegram`

- Generálás a wal palettájával és egy megadott háttérképpel:

`wal-telegram --background={{path/to/image}}`

- Generálás a wal palettájával és a palettán alapuló színes háttérrel:

`wal-telegram --tiled`

- Alkalmazza a háttérképre a gauss elmosódást:

`wal-telegram -g`

- A generált téma helyének megadása (alapértelmezett: `$XDG_CACHE_HOME/wal-telegram` vagy `~/.cache/wal-telegram`):

`wal-telegram --destination={{path/to/destination}}`

- A generálás után indítsa újra a telegram alkalmazást:

`wal-telegram --restart`
