# picom-trans

> A `picom` ablakkompozitáló ablak átlátszatlanságának beállítása. További információ: <https://github.com/yshui/picom>.

- Az aktuálisan fókuszált ablak átlátszatlanságának beállítása egy adott százalékos értékre:

`picom-trans --current --opacity {{90}}`

- Egy adott nevű ablak átlátszatlanságának beállítása:

`picom-trans --name {{Firefox}} --opacity {{90}}`

- Az egérkurzorral kiválasztott konkrét ablak átlátszatlanságának beállítása:

`picom-trans --select --opacity {{90}}`

- Egy adott ablak átlátszatlanságának átkapcsolása:

`picom-trans --name {{Firefox}} --toggle`
