# b3sum

> Calcule les sommes de contrôle cryptographiques BLAKE3.
> Plus d'informations : <https://github.com/BLAKE3-team/BLAKE3/tree/master/b3sum>.

- Calcule la somme de contrôle BLAKE3 pour un ou plusieurs fichiers :

`b3sum {{chemin/vers/fichier1 chemin/vers/fichier2 ...}}`

- Calcule et enregistre la liste des sommes de contrôle BLAKE3 dans un fichier :

`b3sum {{chemin/vers/fichier1 chemin/vers/fichier2 ...}} > {{chemin/vers/fichier.b3}}`

- Calculer une somme de contrôle BLAKE3 à partir de `stdin` :

`{{commande}} | b3sum`

- Lit un fichier de sommes et de noms de fichiers BLAKE3 et vérifie que tous les fichiers ont des sommes de contrôle correspondantes :

`b3sum --check {{chemin/vers/fichier.b3}}`

- N'affiche un message que pour les fichiers manquants ou en cas d'échec de la vérification :

`b3sum --check --quiet {{chemin/vers/fichier.b3}}`
