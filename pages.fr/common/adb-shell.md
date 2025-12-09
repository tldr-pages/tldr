# adb shell

> Android Debug Bridge Shell: Exécute une commande shell sur une instance d'émulateur Android ou un appareil Android.
> Plus d'informations : <https://developer.android.com/tools/adb>.

- Démarre une session shell interactive sur l'émulateur/l'appareil :

`adb shell`

- Récupère toutes les propriétés depuis un émulateur ou un appareil :

`adb shell getprop`

- Remet toutes les permissions courante à leurs valeurs par défaut :

`adb shell pm reset-permissions`

- Révoque une permission dangereuse pour une application :

`adb shell pm revoke {{paquet}} {{permission}}`

- Déclenche un événement clé :

`adb shell input keyevent {{code}}`

- Nettoie les données d'une application sur un émulateur ou un appareil :

`adb shell pm clear {{paquet}}`

- Démarre une activité sur un émulateur ou un appareil :

`adb shell am start -n {{paquet}}/{{activité}}`

- Démarre une activité maison depuis un émulateur ou un appareil :

`adb shell am start -W -c android.intent.category.HOME -a android.intent.action.MAIN`
