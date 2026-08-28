# ufw status

> Affiche l’état de pare-feu simple et ses règles.
> Plus d’informations : <https://manned.org/ufw>.

- Affiche si le pare-feu est actif et liste les règles :

`sudo ufw status`

- Affiche les règles avec leurs numéros (utile avant de supprimer une règle par son numéro) :

`sudo ufw status numbered`

- Affiche l’état détaillé, notamment les politiques par défaut et les ports en écoute :

`sudo ufw status verbose`
