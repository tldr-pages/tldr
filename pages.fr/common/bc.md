# bc

> Un langage de calcul de précision arbitraire.
> Voir aussi : `dc`.
> Plus d'informations : <https://manned.org/man/bc.1>.

- Démarre une session interactive :

`bc`

- Démarre une session interactive avec la bibliothèque mathématique standard activée :

`bc --mathlib`

- Calcule une expression :

`echo '{{5 / 3}}' | bc`

- Exécute un script :

`bc {{chemin/vers/le/script.bc}}`

- Calcule une expression avec l'échelle spécifiée :

`echo 'scale = {{10}}; {{5 / 3}}' | bc`

- Calcule une fonction sinus/cosinus/arctangente/logarithme naturel/exponentielle en utilisant `mathlib` :

`echo '{{s|c|a|l|e}}({{1}})' | bc --mathlib`
