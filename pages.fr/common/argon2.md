# argon2

> Calcule les hachés cryptographiques d'Argon2.
> Plus d'informations : <https://github.com/P-H-C/phc-winner-argon2#command-line-utility>.

- Calcule un haché avec un mot de passe et un sel avec les paramètres par défaut :

`echo "{{mot_de_passe}}" | argon2 "{{sel}}"`

- Calcule un haché avec l'algorithme spécifié :

`echo "{{mot_de_passe}}" | argon2 "{{sel}}" -{{d|i|id}}`

- Affiche le haché de sortie sans informations supplémentaires :

`echo "{{mot_de_passe}}" | argon2 "{{sel}}" -e`

- Calcule un haché avec des [t]emps d'itération, l'utilisation de la [m]émoire et des paramètres de [p]arallélisme donnés :

`echo "{{mot_de_passe}}" | argon2 "{{sel}}" -t {{5}} -m {{20}} -p {{7}}`
