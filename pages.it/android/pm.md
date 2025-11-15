# pm

> Mostra informazioni sulle applicazioni su un dispositivo Android.
> Maggiori informazioni: <https://developer.android.com/tools/adb#pm>.

- Elenca tutte le app installate:

`pm list packages`

- Elenca tutte le app di sistema installate:

`pm list packages -s`

- Elenca tutte le app di terze parti installate:

`pm list packages -3`

- Elenca le app che corrispondono a parole chiave specifiche:

`pm list packages {{parola_chiave1 parola_chiave2 ...}}`

- Mostra il percorso dell'APK di una specifica app:

`pm path {{app}}`
