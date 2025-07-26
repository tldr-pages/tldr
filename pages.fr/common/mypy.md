# mypy

> Vérifie les types dans un code Python.
> Plus d'informations : <https://mypy.readthedocs.io/en/stable/running_mypy.html>.

- Vérifie les types pour un fichier spécifique :

`mypy {{chemin/vers/fichier.py}}`

- Vérifie les types pour un module :

`mypy {{[-m|--module]}} {{nom_module}}`

- Vérifie les types pour un paquet :

`mypy {{[-p|--package]}} {{nom_paquet}}`

- Vérifie les types pour une chaîne de code :

`mypy {{[-c|--command]}} "{{code}}"`

- Ignore les imports manquants :

`mypy --ignore-missing-imports {{chemin/vers/fichier_ou_dossier}}`

- Montre le détail des messages d'erreurs :

`mypy {{[--tb|--show-traceback]}} {{chemin/vers/fichier_ou_dossier}}`

- Spécifie un fichier de configuration :

`mypy --config-file {{chemin/vers/fichier_de_configuration}}`

- Affiche l'aide :

`mypy {{[-h|--help]}}`
