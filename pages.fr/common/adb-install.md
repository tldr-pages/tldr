# adb install

> Android Debug Bridge Install: Pousse des paquets vers une instance d'émulateur Android ou un appareil Android.
> Plus d'informations : <https://developer.android.com/tools/adb>.

- Pousse une application Android vers l'émulateur/l'appareil :

`adb install {{chemin/vers/fichier}}.apk`

- Pousse une application Android vers l'émulateur/l'appareil spécifique via son numéro de série (écrase la variable `$ANDROID_SERIAL`) :

`adb -s {{numéro_série}} install {{chemin/vers/fichier}}.apk`

- Réinstalle une application existante, tout en gardant ses données :

`adb install -r {{chemin/vers/fichier}}.apk`

- Pousse une application Android en autorisant la rétrogradation de version (uniquement pour les paquets debuggable) :

`adb install -d {{chemin/vers/fichier}}.apk`

- Accorde toutes les permissions listées dans le manifeste de l'application :

`adb install -g {{chemin/vers/fichier}}.apk`

- Met à jour rapidement un paquet en mettant à jour uniquement les parties de l'APK qui ont changé :

`adb install --fastdeploy {{chemin/vers/fichier}}.apk`
