# adb shell pm list packages

> Elenca pacchetti installati, conosciuti o filtrati su un dispositivo Android.
> Maggiori informazioni: <https://developer.android.com/tools/adb>.

- Elenca tutti i pacchetti installati:

`adb shell pm list packages`

- Elenca tutti i pacchetti con i relativi percorsi dei file APK:

`adb shell pm list packages -f`

- Elenca solo i pacchetti disabilitati:

`adb shell pm list packages -d`

- Elenca solo i pacchetti abilitati:

`adb shell pm list packages -e`

- Elenca solo i pacchetti di sistema:

`adb shell pm list packages -s`

- Elenca solo i pacchetti di terze parti (non di sistema):

`adb shell pm list packages -3`

- Mostra l'installer per ogni pacchetto:

`adb shell pm list packages -i`
