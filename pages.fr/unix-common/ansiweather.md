# ansiweather

> Un script Shell pour afficher les conditions météo actuelles dans votre terminal.
> Plus d'informations : <https://github.com/fcambus/ansiweather>.

- Affiche une prévision avec le système métrique pour les 5 prochains jours dans la ville de Paris, France :

`ansiweather -u {{metric}} -f {{5}} -l {{Paris,FR}}`

- Affiche une prévision avec des symboles et les données d'ensoleillement pour votre position actuelle :

`ansiweather -s {{true}} -d {{true}}`

- Affiche une prévision avec les données sur le vent et l'humidité pour votre position actuelle :

`ansiweather -w {{true}} -h {{true}}`
