# adb forward

> Se connecte à un appareil Android sans fil.
> Plus d'informations : <https://developer.android.com/tools/adb>.

- Redirige un port TCP :

`adb forward tcp:{{port_local}} tcp:{{port_distant}}`

- Liste toutes les redirections :

`adb forward --list`

- Supprime une règle de redirection :

`adb forward --remove tcp:{{port_local}}`

- Supprime toutes les redirections :

`adb forward --remove-all`
