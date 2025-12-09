# adb

> Android Debug Bridge: komunikuj się z instancją emulatora Androida lub podłączonym urządzeniem z Androidem.
> Niektóre podkomendy takie jak `shell` mają osobną dokumentację.
> Więcej informacji: <https://developer.android.com/tools/adb>.

- Sprawdź czy proces serwera adb działa, jeśli nie, uruchom go:

`adb start-server`

- Zakończ proces serwera adb:

`adb kill-server`

- Uruchom powłokę w docelowej instancji emulatora/urządzenia:

`adb shell`

- Wyślij aplikację Android do emulatora/urządzenia:

`adb install -r {{ścieżka/do/pliku.apk}}`

- Skopiuj plik/katalog z urządzenia docelowego:

`adb pull {{ścieżka/do/pliku_lub_katalogu_na_urządzeniu}} {{ścieżka/do/lokalnego_katalogu_docelowego}}`

- Skopiuj plik/katalog do urządzenia docelowego:

`adb push {{ścieżka/do/lokalnego_pliku_lub_katalogu}} {{ścieżka/do/docelowego_katalogu_na_urządzeniu}}`

- Wypisz wszystkie połączone urządzenia:

`adb devices`
