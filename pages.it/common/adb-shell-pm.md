# adb shell pm

> Strumento Android pacchetto Manager.
> Maggiori informazioni: <https://developer.android.com/tools/adb>.

- Elenca i pacchetti installati:

`adb shell pm list packages`

- Installa un pacchetto app da un percorso specificato:

`adb shell pm install /{{percorso/all/app.apk}}`

- Disinstalla un pacchetto dal dispositivo:

`adb shell pm uninstall {{pacchetto}}`

- Cancella tutti i dati dell'app per un pacchetto:

`adb shell pm clear {{pacchetto}}`

- Abilita un pacchetto o componente:

`adb shell pm enable {{pacchetto_or_classe}}`

- Disabilita un pacchetto o componente:

`adb shell pm disable-user {{pacchetto_or_classe}}`

- Concede un permesso per un'app:

`adb shell pm grant {{pacchetto}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`

- Revoca un permesso per un'app:

`adb shell pm revoke {{pacchetto}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`
