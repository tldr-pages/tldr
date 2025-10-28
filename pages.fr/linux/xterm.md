# xterm

> Emulateur de terminal pour le système de fenêtrage X Window System.
> Plus d'informations : <https://manned.org/xterm>.

- Ouvre une nouvelle fenêtre de terminal ayant pour titre `Exemple` :

`xterm -T {{Exemple}}`

- Ouvre une nouvelle fenêtre de terminal en mode plein écran :

`xterm -fullscreen`

- Ouvre une fenêtre de terminal avec un fond d'écran bleu sombre (`darkblue`) et une couleur de police jaune (`yellow`) :

`xterm -bg {{darkblue}} -fg {{yellow}}`

- Ouvre une fenêtre de terminal de 100 charactères de large (par ligne) et 35 lignes de hauteur, positionnée sur l'écran au point x=200px, y=20px :

`xterm -geometry {{100}}x{{35}}+{{200}}+{{20}}`

- Ouvre une fenêtre de teminal en utilisant la police `Serif` en taille 20 :

`xterm -fa {{'Serif'}} -fs {{20}}`
