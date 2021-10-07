# yes

> Envoie un message à répétition en sortie console.
> Cette commande est souvent utilisée pour éviter de devoir accepter des opérations successives (par exemple des installations via la commande `apt-get`).
> Plus d'informations : <https://www.gnu.org/software/coreutils/yes>.

- Envoyer « message » à répétition :

`yes {{message}}`

- Envoyer « y » à répétition :

`yes`

- Répondre « oui » à toutes les questions posées par la commande `apt-get` :

`yes | sudo apt-get install {{program}}`
