# tput

> Accède et modifie les paramètres du terminal.
> Plus d'informations : <https://manned.org/tput>.

- Déplace le curseur à un endroit donné sur l'écran :

`tput cup {{coordonnée_y}} {{coordonnée_x}}`

- Règle la couleur de l'avant-plan (af) ou de l'arrière-plan (ab) :

`tput {{setaf|setab}} {{code_de_couleur_ANSI}}`

- Affiche le numéro de colonnes, de rangées, ou de couleurs :

`tput {{cols|lines|colors}}`

- Active la sonnerie du terminal :

`tput bel`

- Réinitialise tous les attributs du terminal :

`tput sgr0`

- Active ou désactive le retour automatique à la ligne :

`tput {{smam|rmam}}`
