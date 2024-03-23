# adb reverse

> Android Debug Bridge Reverse: zwrotne połączenie socketowe z emulowanego lub prawdziwego urządzenia Android.
> Więcej informacji: <https://developer.android.com/tools/adb>.

- Listuj wszystkie zwrotne połączenia socketowe z emulatorów i urządzeń:

`adb reverse --list`

- Przekieruj port TCP z emulatora lub urządzenia do localhost:

`adb reverse tcp:{{remote_port}} tcp:{{local_port}}`

- Usuń wybrane zwrotne połączenie z emulatora lub urządzenia:

`adb reverse --remove tcp:{{remote_port}}`

- Usuń wszystkie zwrotne połączenie z emulatorów lub urządzeń:

`adb reverse --remove-all`
