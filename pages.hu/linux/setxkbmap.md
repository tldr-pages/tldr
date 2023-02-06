# setxkbmap

> A billentyűzet beállítása az X Keyboard Extension segítségével. További információ: <https://manned.org/setxkbmap>.

- Állítsa be a billentyűzetet francia AZERTY-re:

`setxkbmap {{fr}}`

- Több billentyűzetkiosztás, azok változatainak és váltási lehetőségének beállítása:

`setxkbmap -layout {{us,de}} -variant {{,qwerty}} -option {{'grp:alt_caps_toggle'}}`

- Segítség kérése:

`setxkbmap -help`

- Az összes elrendezés listázása:

`localectl list-x11-keymap-layouts`

- Az elrendezés változatainak listázása:

`localectl list-x11-keymap-variants {{de}}`

- A rendelkezésre álló kapcsolási lehetőségek listája:

`localectl list-x11-keymap-options | grep grp:`
