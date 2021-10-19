# node

> Plateforme JavaScript côté serveur.
> Plus d'informations : <https://nodejs.org>.

- Éxecute un fichier JavaScript :

`node {{chemin/vers/fichier}}`

- Démarre un REPL (shell interactif) :

`node`

- Évalue du code JavaScript en le passant en argument :

`node -e "{{code}}"`

- Évalue et affiche le résultat, très utile pour voir les versions de dépendances node :

`node -p "{{process.versions}}"`

- Active l'inspecteur, mets en pause l'éxécution jusqu'à ce qu'un debugger soit connecté une fois que le code source est totalement interprété :

`node --no-lazy --inspect-brk {{chemin/vers/fichier}}`
