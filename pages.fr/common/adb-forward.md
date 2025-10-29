# adb forward

> Se connecte à un appareil Android sans fil.
> Plus d'informations : <https://developer.android.com/tools/adb>.

- Redirige un port TCP vers le seul émulateur ou appareil connecté :

`adb forward tcp:{{port_local}} tcp:{{port_distant}}`

- Redirige un port TCP vers un émulateur ou appareil spécifique (identifié par ID / numéro de [s]érie):

`adb -s {{device_ID}} forward tcp:{{local_port}} tcp:{{remote_port}}`

- Liste toutes les redirections :

`adb forward --list`

- Supprime une règle de redirection :

`adb forward --remove tcp:{{port_local}}`

- Supprime toutes les redirections :

`adb forward --remove-all`
