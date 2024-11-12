# xset

> User preference utility for X.
> More information: <https://manned.org/xset>.

- Disable the screensaver:

`xset s off`

- Disable the bell sound:

`xset b off`

- Set the screensaver to start after 60 minutes of inactivity:

`xset s 3600 3600`

- Disable DPMS (Energy Star) features:

`xset -dpms`

- Enable DPMS (Energy Star) features:

`xset +dpms`

- Query information on any X server:

`xset -display :{{0}} q`
