# androguard

> Outil d’ingénierie inverse pour les applications Android. Écrit en Python.
> Plus d'informations : <https://github.com/androguard/androguard>.

- Affiche le manifest d'application Android :

`androguard axml {{chemin/vers/application}}.apk`

- Affiche les métadonnées de l'application (version et ID d'application) :

`androguard apkid {{chemin/vers/application}}.apk`

- Décompile le code Java de l'application :

`androguard decompile {{chemin/vers/application}}.apk --output {{chemin/vers/répertoire}}`
