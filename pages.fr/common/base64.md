# base64

> Encoder ou décoder un fichier ou l'entrée standard en utilisant le codage Base64 à destination de la sortie standard.

- Encoder un fichier :

`base64 {{fichier}}`

- Decode a file :

`base64 -d {{fichier}}`

- Encoder depuis `stdin` :

`{{une_commande}} | base64`

- Décoder depuis `stdin` :

`{{une_commande}} | base64 -d`
