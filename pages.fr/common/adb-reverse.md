# adb reverse

> Android Debug Bridge Reverse: Transfère des connections réseaux depuis une instance d'émulateur Android ou un appareil Android.
> Plus d'informations : <https://developer.android.com/tools/adb>.

- Affiche la liste de toutes les connections réseaux qui sont transféré depuis les émulateurs ou les appareils :

`adb reverse --list`

- Transfère un port TCP depuis un émulateur ou un appareil vers localhost :

`adb reverse tcp:{{port_distant}} tcp:{{port_local}}`

- Supprime une connection socket en cours depuis un émulateur ou un appareil :

`adb reverse --remove tcp:{{port_distant}}`

- Supprime toutes les connections socket depuis tous les émulateurs et appareils :

`adb reverse --remove-all`
