# adb reverse

> Android Debug Bridge Reverse: conexiuni cu soclu invers de la o instanță emulator Android sau dispozitive Android conectate.
> Mai multe informaţii: <https://developer.android.com/studio/command-line/adb>

- Listează toate conexiunile soclu inversă de la emulatori și dispozitive:

`adb reverse --list`

- Inversați un port TCP de la un emulator sau dispozitiv la localhost:

`adb reverse tcp:{{remote_port}} tcp:{{local_port}}`

- Scoateți o conexiune soclu inversă de la un emulator sau dispozitiv:

`adb reverse --remove tcp:{{remote_port}}`

- Eliminați toate conexiunile soclu inversat de la toate emulatoarele și dispozitivele:

`adb reverse --remove-all`
