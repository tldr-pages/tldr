# adb shell pm

> Gestionnaire de Paquets d'Android.
> Plus d'informations : <https://developer.android.com/tools/adb>.

- Liste les paquets installés :

`adb shell pm list packages`

- Installe une application depuis un chemin donné :

`adb shell pm install /{{chemin/vers/fichier.apk}}`

- Déinstalle un paquet de l'appareil :

`adb shell pm uninstall {{paquet}}`

- Supprime les données d'une application :

`adb shell pm clear {{paquet}}`

- Active une application ou un composant :

`adb shell pm enable {{paquet_ou_classe}}`

- Désactive une application ou un composant :

`adb shell pm disable-user {{paquet_ou_classe}}`

- Donne une permission à une application :

`adb shell pm grant {{paquet}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`

- Révoque une permission d'une application:

`adb shell pm revoke {{paquet}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`
