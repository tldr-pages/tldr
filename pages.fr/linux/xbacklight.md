# xbacklight

> Outil pour ajuster la luminosité du rétroéclairage en utilisant l'extension RandR.
> Plus d'informations : <https://gitlab.freedesktop.org/xorg/app/xbacklight>.

- Obtient le niveau de luminosité de l'écran actuel comme un pourcentage :

`xbacklight`

- Régle la luminosité de l'écran à 40% :

`xbacklight -set {{40}}`

- Augmente la luminosité de l'écran actuel de 25% :

`xbacklight -inc {{25}}`

- Diminue la luminosité de l'écran actuel de 75% :

`xbacklight -dec {{75}}`

- Augment la luminosité de l'écran à 100%, étendu sur 60 secondes (valeur donnée en ms), en 60 pas :

`xbacklight -set {{100}} -time {{60000}} -steps {{60}}`
