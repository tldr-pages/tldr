# bun

> Moteur d'exécution et boîte à outils JavaScript.
> Comprend un empaqueteur, un exécuteur de tests et un gestionnaire de paquets.
> Plus d'informations : <https://bun.sh>.

- Exécute un fichier JavaScript ou un script référencé dans `package.json` :

`bun run {{chemin/vers/fichier|nom_script}}`

- Exécute les tests unitaires :

`bun test`

- Télécharge et installe tous les paquets listés comme dépendances dans `package.json` :

`bun install`

- Ajoute une dépendance à `package.json` :

`bun add {{nom_module}}`

- Supprime une dépendance de `package.json` :

`bun remove {{nom_module}}`

- Crée un nouveau projet Bun dans le répertoire actuel :

`bun init`

- Démarre un REPL (shell interactif) :

`bun repl`

- Met à jour Bun vers la dernière version :

`bun upgrade`
