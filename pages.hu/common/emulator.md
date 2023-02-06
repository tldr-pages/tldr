# emulator

> Android emulátorok kezelése a parancssorból. További információ: <https://developer.android.com/studio/run/emulator-commandline>.

- A súgó megjelenítése:

`emulator -help`

- Android emulátor eszköz indítása:

`emulator -avd {{name}}`

- Az emulációhoz rendelkezésre álló webkamerák megjelenítése a fejlesztő számítógépen:

`emulator -avd {{name}} -webcam-list`

- Indítson el egy emulátort, amely felülbírálja a hátlapi kamerával szemben lévő beállítást (használja a `-camera-front` az előlapi kamerához):

`emulator -avd {{name}} -camera-back {{none|emulated|webcamN}}`

- Indítson el egy emulátort, maximális hálózati sebességgel:

`emulator -avd {{name}} -netspeed {{gsm|hscsd|gprs|edge|hsdpa|lte|evdo|full}}`

- Indítson el egy emulátort hálózati késleltetéssel:

`emulator -avd {{name}} -netdelay {{gsm|hscsd|gprs|edge|hsdpa|lte|evdo|none}}`

- Emulátor indítása, az összes TCP-kapcsolatot egy megadott HTTP/HTTPS-proxyn keresztül létrehozva (a port száma szükséges):

`emulator -avd {{name}} -http-proxy {{http://example.com:80}}`

- Emulátor indítása egy adott SD-kártya partíció képfájllal:

`emulator -avd {{name}} -sdcard {{path/to/sdcard.img}}`
