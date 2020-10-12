# yes

> Envoie un message à répétition en sortie console.
> Cette commande est souvent utilisée pour éviter de devoir accepter des opérations successives.
> (par exemple des installations via la commande `apt-get`).

- Envoyer «message» à répétition:

`yes {{message}}`

- Envoyer «y» à répétition:

`yes`

- Accepter tout ce qui est demandé par la commande `sudo apt-get`:

`yes | sudo apt-get install {{program}}`
