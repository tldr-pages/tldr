# adb shell pm list

> Liste les utilisateurs, paquets, permissions, l'instrumentation, les groupes de permissions, les fonctionnalités et les bibliothèques gérées par le gestionnaire de paquets.
> Plus d'informations : <https://developer.android.com/tools/adb>.

- Liste les paquets installés :

`adb shell pm list packages`

- Affiche les utilisateurs sur le système :

`adb shell pm list users`

- Affiche tout les groupes de permissions connus :

`adb shell pm list permission-groups`

- Affiche toutes les permissions connues :

`adb shell pm list permissions`

- Affiche tout les paquets de test :

`adb shell pm list instrumentation`

- Affiche toutes les fonctionnalités du système :

`adb shell pm list features`

- Affiche toutes les bibliothèques supportées par l'appareil courant :

`adb shell pm list libraries`
