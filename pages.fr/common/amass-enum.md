# amass enum

> Trouve les sous-domaines d'un domaine.
> Plus d'informations : <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-enum-subcommand>.

- Trouve les sous-domaines d'un domaine passivement :

`amass enum -passive -d {{nom_de_domaine}}`

- Trouve les sous-domaines d'un domaine et les verifie activement en essayant de résoudre les sous-domaines trouvés :

`amass enum -active -d {{nom_de_domaine}} -p {{80,443,8080}}`

- Fait recherche par force brute pour les sous-domaines :

`amass enum -brute -d {{nom_de_domaine}}`

- Sauvegarde les résultats vers un fichier texte :

`amass enum -o {{fichier_de_sortie}} -d {{nom_de_domaine}}`

- Sauvegarde les résultats dans une base de données :

`amass enum -o {{fichier_de_sortie}} -dir {{chemin/vers/la_base_de_données}}`
