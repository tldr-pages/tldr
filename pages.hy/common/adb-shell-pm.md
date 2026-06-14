# adb shell pm

> Android փաթեթների կառավարիչ գործիք:.
> Լրացուցիչ տեղեկություններ. <https://developer.android.com/tools/adb>:.

- Տեղադրված փաթեթների ցանկ.:

`adb shell pm list packages`

- Տեղադրեք հավելվածի փաթեթ տվյալ ճանապարհից.:

`adb shell pm install /{{path/to/app}}.apk`

- Հեռացրեք փաթեթը սարքից.:

`adb shell pm uninstall {{package}}`

- Մաքրել բոլոր հավելվածների տվյալները փաթեթի համար.:

`adb shell pm clear {{package}}`

- Միացնել փաթեթը կամ բաղադրիչը.:

`adb shell pm enable {{package_or_class}}`

- Անջատել փաթեթը կամ բաղադրիչը.:

`adb shell pm disable-user {{package_or_class}}`

- Թույլտվություն տրամադրեք հավելվածի համար.:

`adb shell pm grant {{package}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`

- Չեղյալ համարել հավելվածի թույլտվությունը.:

`adb shell pm revoke {{package}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`
