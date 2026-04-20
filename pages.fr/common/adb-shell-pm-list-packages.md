# adb shell pm list packages

> Liste les paquets installés, connus, ou filtrés sur un appareil Android.
> Plus d'informations : <https://developer.android.com/tools/adb>.

- Liste tout les paquets installés :

`adb shell pm list packages`

- Liste tout les paquets et les chemins de leurs [f]ichiers APK associés :

`adb shell pm list packages -f`

- Liste seulement les paquets [d]ésactivés :

`adb shell pm list packages -d`

- Liste seulement les paquets activ[é]s :

`adb shell pm list packages -e`

- Liste seulement les paquets [s]ystème :

`adb shell pm list packages -s`

- Liste seulement les paquets tiers (hors système) :

`adb shell pm list packages -3`

- Affiche l'[i]nstallateur pour chaque paquet :

`adb shell pm list packages -i`
