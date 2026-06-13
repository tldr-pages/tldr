# dumpsys

> Fourni des informations sur les services du système Android.
> Cette commande peut être utilisé uniquement depuis `adb shell`.
> Plus d'informations : <https://developer.android.com/tools/dumpsys>.

- Récupère un diagnostic pour chaque service système :

`dumpsys`

- Récupère un diagnostic pour un service système spécifique :

`dumpsys {{service}}`

- Liste tous les services dont `dumpsys` peut donner les informations :

`dumpsys -l`

- Liste les arguments spécifiques d'un service :

`dumpsys {{service}} -h`

- Exclus un service spécifique d'un diagnostic :

`dumpsys --skip {{service}}`

- Spécifie un temps limite en secondes (10s par défaut) :

`dumpsys -t {{seconds}}`
