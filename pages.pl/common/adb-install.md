# adb install

> Android Debug Bridge Install: wysyłaj pakiety do instancji emulatora Androida lub podłączonych urządzeń z systemem Android.
> Więcej informacji: <https://developer.android.com/tools/adb>.

- Wyślij aplikację na Androida do emulatora/urządzenia:

`adb install {{ścieżka/do/pliku.apk}}`

- Wyślij aplikację Android do określonego emulatora/urządzenia (nadpisuje `$ANDROID_SERIAL`):

`adb -s {{numer_seryjny}} install {{ścieżka/do/pliku.apk}}`

- Zainstaluj ponownie ([r]einstall) istniejącą aplikację, zachowując jej dane:

`adb install -r {{ścieżka/do/pliku.apk}}`

- Wyślij aplikację na Androida, umożliwiając obniżenie ([d]owngrade) wersji kodu (tylko pakiety debugowalne):

`adb install -d {{ścieżka/do/pliku.apk}}`

- Przyznaj ([g]rant) wszystkie uprawnienia wymienione w pliku manifestu aplikacji:

`adb install -g {{ścieżka/do/pliku.apk}}`

- Szybko zaktualizuj zainstalowany pakiet, aktualizując tylko te części APK, które się zmieniły:

`adb install --fastdeploy {{ścieżka/do/pliku.apk}}`
