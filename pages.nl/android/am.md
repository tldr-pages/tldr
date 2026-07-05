# am

> Android-activiteitenmanager.
> Meer informatie: <https://developer.android.com/tools/adb#am>.

- Start een specifieke activiteit:

`am start -n {{com.android.settings/.Settings}}`

- Start een activiteit en geef er gegevens aan door:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Start een activiteit die overeenkomt met een specifieke [a]ctie en [c]ategorie:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Converteer een intentie naar een URI:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Start de home-activiteit op een emulator of apparaat:

`am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
