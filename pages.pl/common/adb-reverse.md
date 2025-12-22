# adb reverse

> Android Debug Bridge Reverse: zwrotne połączenie socketowe z emulowanego lub prawdziwego urządzenia Android.
> Więcej informacji: <https://developer.android.com/tools/adb>.

- Wypisz wszystkie zwrotne połączenia socketowe z emulatorów i urządzeń:

`adb reverse --list`

- Przekieruj port TCP z emulatora lub urządzenia do localhost:

`adb reverse tcp:{{zdalny_port}} tcp:{{lokalny_port}}`

- Usuń wybrane zwrotne połączenie z emulatora lub urządzenia:

`adb reverse --remove tcp:{{zdalny_port}}`

- Usuń wszystkie zwrotne połączenia z wszystkich emulatorów lub urządzeń:

`adb reverse --remove-all`
