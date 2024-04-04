# adb install

> Android Debug Bridge Install: wysyłaj pakiety do instancji emulatora Androida lub podłączonych urządzeń z systemem Android.
> Więcej informacji: <https://developer.android.com/tools/adb>.

- Wyślij aplikację na Androida do emulatora / urządzenia:

`adb install {{scieżka/do/pliku.apk}}`

- Zainstaluj ponownie istniejącą aplikację, zachowując jej dane:

`adb install -r {{scieżka/do/pliku.apk}}`

- Przyznaj wszystkie uprawnienia wymienione w pliku manifestu aplikacji:

`adb install -g {{scieżka/do/pliku.apk}}`

- Szybko zaktualizuj zainstalowany pakiet, aktualizując tylko te części APK, które się zmieniły:

`adb install --fastdeploy {{scieżka/do/pliku.apk}}`
