# maim

> Pillanatkép segédprogram. További információ: <https://github.com/naelstrof/maim>.

- Képernyőkép készítése és mentése a megadott elérési útvonalra:

`maim {{path/to/screenshot.png}}`

- Képernyőkép készítése a kiválasztott régióról:

`maim --select {{path/to/screenshot.png}}`

- Képernyőkép készítése a kiválasztott régióról és mentése a vágólapra ( `xclip`):

`maim --select | xclip -selection clipboard -target image/png`

- Képernyőkép készítése az aktuálisan aktív ablakról ( `xdotool`):

`maim --window $(xdotool getactivewindow) {{path/to/screenshot.png}}`
