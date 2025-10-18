# xterm

> Emulateur de terminal pour le serveur de fenêtres _X Window System_.
> Plus d'informations: <https://manned.org/xterm>.

- Ouvrir une nouvelle fenêtre de terminal ayant pour titre `Exemple`: 

`xterm -T {{Exemple}}`

- Ouvrir une nouvelle fenêtre de terminal en mode plein écran:

`xterm -fullscreen`

- Ouvrir une fenêtre de terminal avec un fond d'écran bleu sombre (_darkblue_) et une couleur de fonte jaune (_yellow_):
 
`xterm -bg {{darkblue}} -fg {{yellow}}`

- Ouvrir une fenêtre de terminal de 100 charactères de large (par ligne) et 35 lignes de hauteur, positionnée sur l'écran au point x=200px, y=20px:
 
`xterm -geometry {{100}}x{{35}}+{{200}}+{{20}}`

- Ouvrir une fenétre de teminal en utilisant la font `Serif` en taille 20:

`xterm -fa {{'Serif'}} -fs {{20}}`
