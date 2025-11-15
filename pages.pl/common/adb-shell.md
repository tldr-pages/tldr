# adb shell

> Android Debug Bridge Shell: uruchamiaj zdalne polecenia powłoki na instancji emulatora Androida lub podłączonych urządzeniach z Androidem.
> Więcej informacji: <https://developer.android.com/tools/adb>.

- Uruchom interaktywną zdalną powłokę na emulatorze lub urządzeniu:

`adb shell`

- Pobierz wszystkie właściwości z emulatora lub urządzenia:

`adb shell getprop`

- Przywróć domyślne ustawienia wszystkich uprawnień uruchamiania:

`adb shell pm reset-permissions`

- Odwołaj niebezpieczne pozwolenie dla aplikacji:

`adb shell pm revoke {{pakiet}} {{pozwolenie}}`

- Wywołaj zdarzenie klawisza:

`adb shell input keyevent {{kod_klawisza}}`

- Wyczyść dane aplikacji na emulatorze lub urządzeniu:

`adb shell pm clear {{pakiet}}`

- Rozpocznij aktywność na emulatorze lub urządzeniu:

`adb shell am start -n {{pakiet}}/{{aktywność}}`

- Rozpocznij aktywność domową na emulatorze lub urządzeniu:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
