# xargs

> Exécute une commande avec des arguments provenant d’un pipe, d’un fichier, etc.
> L’entrée est traitée comme un bloc de texte unique, puis découpée en éléments séparés par des espaces, tabulations, retours à la ligne et fin de fichier.
> Voir aussi : `parallel`.
> Plus d’informations : <https://www.gnu.org/software/findutils/manual/html_mono/find.html#Invoking-xargs>.

- Exécute une commande en utilisant les données d’entrée comme arguments :

`{{arguments_source}} | xargs {{commande}}`

- Exécute plusieurs commandes chaînées sur les données d’entrée :

`{{arguments_source}} | xargs sh -c "{{commande1}} && {{commande2}} | {{commande3}}"`

- Exécute une nouvelle commande pour chaque argument :

`{{arguments_source}} | xargs {{[-n|--max-args]}} 1 {{commande}}`

- Augmente le nombre de processus parallèles à 10 (par défaut : 1 ; 0 = autant que possible) :

`{{arguments_source}} | xargs {{[-P|--max-procs]}} 10 {{[-n|--max-args]}} {{1}} {{commande}}`

- Exécute la commande une fois par ligne d’entrée, en remplaçant le placeholder (ici _) par la ligne :

`{{arguments_source}} | xargs -I _ {{commande}} _ {{optional_extra_arguments}}`

- Demande une confirmation avant exécution (valider avec y ou Y) :

`{{arguments_source}} | xargs {{[-p|--interactive]}} {{commande}}`

- Lit les arguments depuis un fichier :

`xargs {{[-a|--arg-file]}} {{path/to/file}} {{commande}}`

- Permet à la commande d’accéder au terminal pour une entrée interactive :

`{{arguments_source}} | xargs {{[-o|--open-tty]}} {{commande}}`
