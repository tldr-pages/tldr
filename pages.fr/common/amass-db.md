# amass db

> Intéragie avec une base de données Amass.
> Plus d'informations : <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-db-subcommand>.

- Liste toutes les énumérations performées pas la base de données :

`amass db -dir {{chemin/vers/dossier_de_la_base_de_données}} -list`

- Affiche les résultats pour un index d'énumération et un nom de domaine spécifiés :

`amass db -dir {{chemin/vers/dossier_de_la_base_de_données}} -d {{nom_de_domaine}} -enum {{index_depuis_la liste}} -show`

- Liste tous les sous-domaines trouvés pour un domaine inclus dans une énumération :

`amass db -dir {{chemin/vers/dossier_de_la_base_de_données}} -d {{nom_de_domaine}} -enum {{index_depuis_la liste}} -names`

- Affiche un sommaire des sous-domaines inclus dans une énumération :

`amass db -dir {{chemin/vers/dossier_de_la_base_de_données}} -d {{nom_de_domaine}} -enum {{index_depuis_la liste}} -summary`
