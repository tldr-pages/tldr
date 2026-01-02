# dmypy

> Vérifie les types dans du code Python, en utilisant `mypy` dans un démon pour une exécution plus rapide.
> Voir aussi : `mypy`.
> Plus d'informations : <https://mypy.readthedocs.io/en/stable/mypy_daemon.html>.

- Vérifie les types dans un fichier, et démarre le démon s'il n'est pas lancé :

`dmypy check -- {{chemin/vers/fichier.py}}`

- Démarre le démon :

`dmypy start`

- Vérifie les types dans un fichier (nécéssite que le démon soit lancé) :

`dmypy run -- {{chemin/vers/fichier.py}}`

- Arrête le démon :

`dmypy stop`
