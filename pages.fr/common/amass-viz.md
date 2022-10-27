# amass viz

> Visualise les informations recueillies dans graphique de réseau.
> Plus d'informations : <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-viz-subcommand>.

- Génère une visualisation D3.js basé sur la data de la base de données :

`amass viz -d3 -dir {{chemin/vers/la_base_de_données}}`

- Génère un fichier DOT basé sur la data de la base de données :

`amass viz -dot -dir {{chemin/vers/la_base_de_données}}`

- Génère un fichier GEXF basé sur la data de la base de données :

`amass viz -gexf -dir {{chemin/vers/la_base_de_données}}`

- Génère un fichier JSON Graphistry basé sur la data de la base de données :

`amass viz -graphistry -dir {{chemin/vers/la_base_de_données}}`

- Génère un fichier CSV Maltego basé sur la data de la base de données :

`amass viz -maltego -dir {{chemin/vers/la_base_de_données}}`
