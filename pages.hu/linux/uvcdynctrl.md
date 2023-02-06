# uvcdynctrl

> A libwebcam parancssori eszköz az uvcvideo dinamikus vezérlők kezelésére. További információ: <https://manned.org/uvcdynctrl>.

- Az összes elérhető kamera listázása:

`uvcdynctrl -l`

- Megadja a használni kívánt eszközt (alapértelmezett beállítás: `video0`):

`uvcdynctrl -d {{device_name}}`

- List available controls:

`uvcdynctrl -c`

- Új vezérlőérték beállítása (negatív értékek esetén a {{-érték}} előtt adjon hozzá -- értéket):

`uvcdynctrl -s {{control_name}} {{value}}`

- Az aktuális vezérlőérték lekérdezése:

`uvcdynctrl -g {{control_name}}`

- Az aktuális vezérlőelemek állapotának mentése egy fájlba:

`uvcdynctrl -W {{filename}}`

- A vezérlőelemek állapotának betöltése egy fájlból:

`uvcdynctrl -L {{filename}}`
