# xrandr

> A képernyő kimeneteinek méretének, tájolásának és/vagy tükrözésének beállítása. További információ: <https://www.x.org/releases/current/doc/man/man1/xrandr.1.xhtml>.

- A rendszer aktuális állapotának megjelenítése (ismert képernyők, felbontások, ...):

`xrandr --query`

- A lekapcsolt kimenetek letiltása és a csatlakoztatottak engedélyezése alapértelmezett beállításokkal:

`xrandr --auto`

- A DisplayPort 1 felbontásának és frissítési frekvenciájának módosítása 1920x1080, 60Hz-re:

`xrandr --output {{DP1}} --mode {{1920x1080}} --rate {{60}}`

- Állítsa a HDMI2 felbontását 1280x1024-re, és helyezze a DP1 jobb oldalára:

`xrandr --output {{HDMI2}} --mode {{1280x1024}} --right-of {{DP1}}`

- Tiltja le a VGA1 kimenetet:

`xrandr --output {{VGA1}} --off`

- Állítsa az LVDS1 fényerejét 50%-ra:

`xrandr --output {{LVDS1}} --brightness {{0.5}}`
