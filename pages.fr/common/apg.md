# apg

> Crée arbitrairement les mots de passe aléatoires et complexes.
> Plus d'informations : <https://manned.org/apg>.

- Crée des mots de passe aléatoires (la longueur par défaut est 8) :

`apg`

- Crée un mot de passe avec au moins 1 symbole (S), 1 Nombre (N), 1 Majuscule (C), 1 Minuscule (L) :

`apg -M SNCL`

- Crée un mot de passe avec 16 caractères :

`apg -m {{16}}`

- Crée un mot de passe avec une longeur maximum de 16 :

`apg -x {{16}}`

- Crée un mot de passe qui n'apparaît pas dans le dictionnaire (le fichier de dictionnaire doit être donné) :

`apg -r {{fichier_dictionnaire}}`
