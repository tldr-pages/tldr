# pm

> Android Package Manager-hulpprogramma.
> Meer informatie: <https://developer.android.com/tools/adb#pm>.

- Toon geïnstalleerde pakketten:

`pm list packages`

- Installeer een app-pakket van een opgegeven pad:

`pm install /{{pad/naar/app}}.apk`

- Verwijder een pakket van het apparaat:

`pm uninstall {{pakket}}`

- Verwijder alle app-data voor een pakket:

`pm clear {{pakket}}`

- Schakel een pakket of component in:

`pm enable {{pakket_of_class}}`

- Schakel een pakket of component uit:

`pm disable-user {{pakket_of_class}}`

- Geef toestemming aan een app:

`pm grant {{pakket}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`

- Toestemming voor een app intrekken:

`pm revoke {{pakket}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`
