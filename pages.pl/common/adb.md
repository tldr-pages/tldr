# adb

> Android Debug Bridge: komunikuj się z instancją emulatora Androida lub podłączonym urządzeniem z Androidem.
> Więcej informacji: <https://developer.android.com/tools/adb>.

- Sprawdź czy proces serwera adb działa, jeśli nie, uruchom go:

`adb start-server`

- Zakończ proces serwera adb:

`adb kill-server`

- Uruchom powłokę w instancji emulatora lub urządzeniu:

`adb shell`

- Wypchnij aplikację Androidową do instancji emulatora lub urządzenia:

`adb install -r {{ścieżka/do/pliku.apk}}`

- Skopiuj plik/katalog do urządzenia:

`adb pull {{ścieżka/do/pliku_lub_katalogu_na_urządzeniu}} {{ścieżka/do/lokalnego_katalogu}}`

- Skopiuj plik/katalog z urządzenia:

`adb push {{ścieżka/do/pliku_lub_katalogu_na_urządzeniu}} {{ścieżka/do/lokalnego_katalogu}}`

- Listuj połączone lub emulowane urządzenia:

`adb devices`
