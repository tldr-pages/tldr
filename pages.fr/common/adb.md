# adb

> Android Debug Bridge: Communiquer avec une instance d'émulateur Android ou un appareil Android.
> Certaines commandes comme `adb shell` ont leur propre documentation.
> Plus d'informations : <https://developer.android.com/tools/adb>.

- Vérifie si le processus du serveur adb est en fonctionnement et le démarre :

`adb start-server`

- Arrête le processus du serveur adb :

`adb kill-server`

- Démarre un shell distant sur l'émulateur/l'appareil ciblé :

`adb shell`

- Pousse une application Android vers l'émulateur/l'appareil :

`adb install -r {{chemin/vers/le/fichier.apk}}`

- Copie un fichier/dossier depuis l'appareil ciblé :

`adb pull {{chemin/vers/le/fichier_ou_dossier_de_l'appareil}} {{chemin/vers/le/dossier_de_destination_local}}`

- Copie un fichier/dossier vers l'appareil ciblé :

`adb push {{chemin/vers/le/fichier_ou_dossier_local}} {{chemin/vers/le/dossier_de_destination_de_l'appareil}}`

- Récupère une liste des appareils connectés :

`adb devices`
