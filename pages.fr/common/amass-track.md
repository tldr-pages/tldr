# amass track

> Traque les différences entre les énumérations d'un même domaine.
> Plus d'informations : <https://github.com/OWASP/Amass/blob/master/doc/user_guide.md#the-track-subcommand>.

- Affiche la différence entre les deux dernières énumérations d'un domaine donné :

`amass track -dir {{chemin/vers/la_base_de_données}} -d {{nom_de_domaine}} -last 2`

- Affiche la différence entre un certain moment dans le temps et la dernière énumération :

`amass track -dir {{chemin/vers/la_base_de_données}} -d {{nom_de_domaine}} -since {{01/02 15:04:05 2006 MST}}`
