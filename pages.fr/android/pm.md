# pm

> Gestionnaire de Paquets d'Android.
> Plus d'informations : <https://developer.android.com/tools/adb#pm>.

- Liste les paquets installés :

`pm list packages`

- Installe une application depuis un chemin donné :

`pm install /{{chemin/vers/fichier}}.apk`

- Déinstalle un paquet de l'appareil :

`pm uninstall {{paquet}}`

- Supprime les données d'une application :

`pm clear {{paquet}}`

- Active une application ou un composant :

`pm enable {{paquet_ou_classe}}`

- Désactive une application ou un composant :

`pm disable-user {{paquet_ou_classe}}`

- Donne une permission à une application :

`pm grant {{paquet}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`

- Révoque une permission d'une application :

`pm revoke {{paquet}} {{android.permission.CAMERA|android.permission.ACCESS_FINE_LOCATION|android.permission.READ_CONTACTS|...}}`
