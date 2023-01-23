# blurlock

> Egy egyszerű burkolat az i3 képernyőszekrénye körül: `i3lock`, amely elmosja a képernyőt. Lásd még: `i3lock`. További információ: <https://gitlab.manjaro.org/packages/community/i3/i3exit/-/blob/master/blurlock>.

- A képernyő zárolása az aktuális képernyő elmosódott képernyőképével:

`blurlock`

- A képernyő zárolása és a feloldásjelző letiltása (eltávolítja a visszajelzést a billentyű lenyomásakor):

`blurlock --no-unlock-indicator`

- Zárolja a képernyőt, és ne rejtse el az egérmutatót:

`blurlock --pointer {{default}}`

- Zárja le a képernyőt és mutassa a sikertelen bejelentkezési kísérletek számát:

`blurlock --show-failed-attempts`
