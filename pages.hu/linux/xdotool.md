# xdotool

> Parancssori automatizálás X11-hez. További információ: <https://manned.org/xdotool>.

- A futó Firefox ablak(ok) X-Windows ablakazonosítójának lekérdezése:

`xdotool search --onlyvisible --name {{firefox}}`

- Kattintson a jobb egérgombra:

`xdotool click {{3}}`

- Az éppen aktív ablak azonosítójának lekérdezése:

`xdotool getactivewindow`

- Fókuszáljon az 12345 azonosítóval rendelkező ablakra:

`xdotool windowfocus --sync {{12345}}`

- Írjon be egy üzenetet, minden egyes betűnél 500 ms késleltetéssel:

`xdotool type --delay {{500}} "Hello world"`

- Nyomja meg az enter billentyűt:

`xdotool key {{KP_Enter}}`
