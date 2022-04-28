# adb install

> Android Debug Bridge Install: Pousse des paquets vers une instance d'émulateur Android ou un appareil Android.
> Plus d'informations : <https://developer.android.com/studio/command-line/adb>.

- Pousse une application Android vers l'émulateur/l'appareil :

`adb install {{chemin/vers/le/fichier.apk}}`

- Réinstalle une application existante, tout en gardant ses données :

`adb install -r {{chemin/vers/le/fichier.apk}}`

- Accorde toutes les permissions listées dans le manifeste de l'application :

`adb install -g {{chemin/vers/le/fichier.apk}}`

- Mets à jour rapidement un paquet en mettant à jour uniquement les parties de l'APK qui ont changé :

`adb install --fastdeploy {{chemin/vers/le/fichier.apk}}`
