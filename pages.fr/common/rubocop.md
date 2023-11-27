# rubocop

> Lint les fichiers Ruby.
> Plus d'informations : <https://docs.rubocop.org/rubocop/usage/basic_usage.html>.

- Vérifie tous les fichiers du répertoire actuel (y compris les sous-répertoires) :

`rubocop`

- Vérifie un ou plusieurs fichiers ou répertoires spécifiques :

`rubocop {{chemin/vers/fichier}} {{chemin/vers/dossier}}`

- Écrit la sortie dans un fichier :

`rubocop --out {{chemin/vers/fichier}}`

- Affiche la liste des cops (règles de lint) :

`rubocop --show-cops`

- Exclue un cop :

`rubocop --except {{cop_1}} {{cop_2}}`

- Exécute uniquement les cops spécifiés :

`rubocop --only {{cop_1}} {{cop_2}}`

- Corrige automatiquement les fichiers (expérimental) :

`rubocop --auto-correct`
