# xfce4-screenshooter

> Az XFCE4 képernyőkép készítő eszköze. További információ: <https://docs.xfce.org/apps/xfce4-screenshooter/start>.

- Indítsa el a képernyőfotó GUI-t:

`xfce4-screenshooter`

- Készítsen képernyőfotót a teljes képernyőről, és indítsa el a GUI-t, hogy megkérdezze, hogyan tovább:

`xfce4-screenshooter --fullscreen`

- Készítsen képernyőképet a teljes képernyőről, és mentse a megadott könyvtárba:

`xfce4-screenshooter --fullscreen --save {{path/to/directory}}`

- Várjon egy kis időt a képernyőkép készítése előtt:

`xfce4-screenshooter --delay {{seconds}}`

- Képernyőfotó készítése a képernyő egy területéről (kijelölés az egérrel):

`xfce4-screenshooter --region`

- Készítsen képernyőképet az aktív ablakról, és másolja a vágólapra:

`xfce4-screenshooter --window --clipboard`

- Készítsen képernyőképet az aktív ablakról, és nyissa meg egy kiválasztott programmal:

`xfce4-screenshooter --window --open {{gimp}}`
