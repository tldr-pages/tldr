# pm

> Afficher des informations sur les applications d'un appareil Android.
> Plus d'informations : <https://developer.android.com/studio/command-line/adb#pm>.

- Affiche la liste des applications installées :

`pm list packages`

- Affiche une liste de toutes les applications système instalées :

`pm list packages -s`

- Affiche une liste de toutes les applications tierces :

`pm list packages -3`

- Affiche une liste des applications qui correspondent à des mots clés :

`pm list packages {{mots_clés}}`

- Affiche le chemin vers l'APK d'une application spécifique :

`pm path {{application}}`
