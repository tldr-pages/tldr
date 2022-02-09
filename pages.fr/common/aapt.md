# aapt

> Android Asset Packaging Tool.
> Compile et empaquette les ressources d'une application Android.
> Plus d'informations : <https://elinux.org/Android_aapt>.

- Liste les fichiers contenus une archive APK :

`aapt list {{chemin/vers/app.apk}}`

- Affiche les metadatas d'une application (version, autorisations, etc.) :

`aapt dump badging {{chemin/vers/app.apk}}`

- Créé une nouvelle archive APK avec les fichiers venant d'un dossier spécifique :

`aapt package -F {{chemin/vers/app.apk}} {{chemin/vers/le/dossier}}`
