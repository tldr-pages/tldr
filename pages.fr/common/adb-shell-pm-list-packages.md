# adb shell pm list packages

> Liste les paquets installés, connus, ou filtrés sur un appareil Android.
> Plus d'informations : <https://developer.android.com/tools/adb>.

- Liste tout les paquets installés :

`adb shell pm list packages`

- Liste tout les paquets et les chemins de leurs fichiers APK associés :

`adb shell pm list packages -f`

- Liste seulement les paquets désactivés :

`adb shell pm list packages -d`

- Liste seulement les paquets activés :

`adb shell pm list packages -e`

- Liste seulement les paquets système :

`adb shell pm list packages -s`

- Liste seulement les paquets tierces (pas système) :

`adb shell pm list packages -3`

- Affiche l'installateur pour chaque paquet :

`adb shell pm list packages -i`
