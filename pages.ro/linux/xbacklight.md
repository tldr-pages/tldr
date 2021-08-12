# xbacklight

> Utilitar pentru a regla luminozitatea luminii de fundal utilizând extensia RandR.
> Mai multe informaţii: <https://gitlab.freedesktop.org/xorg/app/xbacklight>

- Obțineți luminozitatea curentă a ecranului ca procent:

`xbacklight`

- Setați luminozitatea ecranului la 40%:

`xbacklight -set {{40}}`

- Măriți luminozitatea curentă cu 25%:

`xbacklight -inc {{25}}`

- Reduceți luminozitatea curentă cu 75%:

`xbacklight -dec {{75}}`

- Creșteți lumina de fundal la 100%, peste 60 de secunde (valoarea dată în ms), utilizând 60 de pași:

`xbacklight -set {{100}} -time {{60000}} -steps {{60}}`
