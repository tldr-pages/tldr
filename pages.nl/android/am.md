# am

> Android-activiteitenmanager.
> Meer informatie: <https://developer.android.com/tools/adb#am>.

- Start de activiteit met een specifiek component en pakket[n]aam:

`am start -n {{com.android.settings/.Settings}}`

- Start een intent[a]ctie en geef er [d]ata aan door:

`am start -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Start een activiteit die overeenkomt met een specifieke [a]ctie en [c]ategorie:

`am start -a {{android.intent.action.MAIN}} -c {{android.intent.category.HOME}}`

- Converteer een intent naar een URI:

`am to-uri -a {{android.intent.action.VIEW}} -d {{tel:123}}`

- Start de home-activiteit op een emulator of apparaat:

`am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
