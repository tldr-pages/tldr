# adb shell

> Android Debug Bridge Shell: Rulați comenzi shell la distanță pe o instanță emulator Android sau dispozitive Android conectate.
> Mai multe informaţii: <https://developer.android.com/studio/command-line/adb>

- Porniți o coajă interactivă la distanță pe emulator/dispozitiv:

`adb shell`

- Obțineți toate proprietățile de la emulator sau dispozitiv:

`adb shell getprop`

- Reveniți toate permisiunile de execuție la implicit:

`adb shell pm reset-permissions`

- Revocarea unei permisiuni periculoase pentru o cerere:

`adb shell pm revoke {{package}} {{permission}}`

- Declanşează un eveniment cheie:

`adb shell input keyevent {{keycode}}`

- Ștergeți datele unei aplicații pe un emulator sau dispozitiv:

`adb shell pm clear {{package}}`

- Începeți o activitate pe emulator/dispozitiv:

`adb shell am start -n {{package}}/{{activity}}`

- Porniți activitatea de acasă pe un emulator sau dispozitiv:

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
