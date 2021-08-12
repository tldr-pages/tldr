# xrandr

> Setați dimensiunea, orientarea și/sau reflectarea ieșirilor pentru un ecran.

- Afișați starea curentă a sistemului (ecrane cunoscute, rezoluții, ... ):

`xrandr --query`

- Dezactivați ieșirile deconectate și activați cele conectate cu setări implicite:

`xrandr --auto`

- Modificați rezoluția și frecvența actualizării DisplayPort 1 la 1920x1080, 60Hz:

`xrandr --output {{DP1}} --mode {{1920x1080}} --rate {{60}}`

- Setați rezoluția HDMI2 la 1280x1024 și puneți-o pe dreapta DP1:

`xrandr --output {{HDMI2}} --mode {{1280x1024}} --right-of {{DP1}}`

- Dezactivați ieșirea VGA1:

`xrandr --output {{VGA1}} --off`

- Setați luminozitatea pentru LVDS1 la 50%:

`xrandr --output {{LVDS1}} --brightness {{0.5}}`

- A se vedea informațiile hardware de afișare:

`xrandr -q`
