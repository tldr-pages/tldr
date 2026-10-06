# aapt

> Android Asset Packaging Tool : compile et empaquette les ressources d'une application Android.
> Plus d'informations : <https://manned.org/aapt>.

- Liste les fichiers contenus une archive APK :

`aapt list {{chemin/vers/application}}.apk`

- Affiche les metadatas d'une application (version, autorisations, etc.) :

`aapt dump badging {{chemin/vers/application}}.apk`

- Créé une nouvelle archive APK avec les fichiers venant d'un dossier spécifique :

`aapt package -F {{chemin/vers/application}}.apk {{chemin/vers/répertoire}}`
