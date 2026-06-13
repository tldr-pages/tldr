# pm

> Strumento Android pacchetto Manager.
> Maggiori informazioni: <https://developer.android.com/tools/adb#pm>.

- Elenca i pacchetti installati:

`pm list packages`

- Installa un pacchetto app da un percorso specificato:

`pm install /{{percorso/all/app}}.apk`

- Disinstalla un pacchetto dal dispositivo:

`pm uninstall {{pacchetto}}`

- Cancella tutti i dati dell'app per un pacchetto:

`pm clear {{pacchetto}}`

- Abilita un pacchetto o componente:

`pm enable {{pacchetto_or_classe}}`

- Disabilita un pacchetto o componente:

`pm disable-user {{pacchetto_or_classe}}`

- Concede un permesso per un'app:

`pm grant {{pacchetto}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`

- Revoca un permesso per un'app:

`pm revoke {{pacchetto}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`
