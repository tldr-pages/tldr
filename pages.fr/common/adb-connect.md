# adb connect

> Se connecte à un appareil Android sans fil.
> Plus d'informations : <https://developer.android.com/tools/adb>.

- S'appaire avec un appareil Android (l'adresse et le code d'appairage se trouvent dans les options de développement) :

`adb pair {{adresse_ip}}:{{port}}`

- Se connecte à un appareil Android (le port sera différent de celui de l'appairage) :

`adb connect {{adresse_ip}}:{{port}}`

- Déconnecte un appareil :

`adb disconnect {{adresse_ip}}:{{port}}`
