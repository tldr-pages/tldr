# am

> Gestore delle Attività di Android.
> Maggiori informazioni: <https://developer.android.com/tools/adb#am>.

- Inizia un'attività:

`am start -n {{com.android.settings/.Settings}}`

- Inizia un'attività e e invia dati:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Inizia un'attività corrispondente ad un'azione, e in una categoria delineato:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Converti un intent in un URI:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
