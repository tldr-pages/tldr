# emulator

> Manager emulatori Android din linia de comandă.
> Mai multe informaţii: <https://developer.android.com/studio/run/emulator-commandline>

- Afișează ajutorul:

`emulator -help`

- Porniți un dispozitiv emulator Android:

`emulator -avd {{name}}`

- Afișați webcam-uri pe computerul de dezvoltare care sunt disponibile pentru emulare:

`emulator -avd {{name}} -webcam-list`

- Porniți un emulator care depășește setarea camerei din spate (utilizați `-camera-front` pentru camera frontală):

`emulator -avd {{name}} -camera-back {{none|emulated|webcamN}}`

- Porniți un emulator, cu o viteză maximă de rețea:

`emulator -avd {{name}} -netspeed {{gsm|hscsd|gprs|edge|hsdpa|lte|evdo|full}}`

- Porniți un emulator cu latență de rețea:

`emulator -avd {{name}} -netdelay {{gsm|hscsd|gprs|edge|hsdpa|lte|evdo|none}}`

- Porniți un emulator, făcând toate conexiunile TCP printr-un proxy HTTP/HTTPS specificat (numărul portului este necesar):

`emulator -avd {{name}} -http-proxy {{http://example.com:80}}`

- Porniți un emulator cu un fișier de imagine de partiție card SD dat:

`emulator -avd {{name}} -sdcard {{path/to/sdcard.img}}`
