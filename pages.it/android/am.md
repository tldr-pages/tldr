# am

> Gestione delle attività di Android.
> Maggiori informazioni: <https://developer.android.com/tools/adb#am>.

- Avvia l'activity con un componente specifico e [n]ome del pacchetto:

`am start -n {{com.android.settings/.Settings}}`

- Avvia un'intent [a]ction e passa [d]ati ad essa:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Avvia un'activity che corrisponde a un'[a]zione e una [c]ategoria specifica:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Converte un intent in un URI:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Avvia l'activity home su un emulatore o dispositivo:

`am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
