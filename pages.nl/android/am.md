# am

> Android-activiteitenmanager.
> Meer informatie: <https://developer.android.com/studio/command-line/adb#am>.

- Start een specifieke activiteit:

`am start -n {{com.android.settings/.Settings}}`

- Start een activiteit en geef er gegevens aan door:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Start een activiteit die overeenkomt met een specifieke actie en categorie:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Converteer een intentie naar een URI:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`
