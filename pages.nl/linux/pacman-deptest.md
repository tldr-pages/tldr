# pacman --deptest

> Controleer elke opgegeven afhankelijkheid en retourneer een lijst met afhankelijkheden die momenteel niet zijn voldaan op het systeem.
> Zie ook: `pacman`.
> Meer informatie: <https://manned.org/pacman.8>.

- Toon de pakket-namen van de afhankelijkheden welke niet geïnstalleerd zijn:

`pacman -T {{pakket1 pakket2 ...}}`

- Controleer of het geïnstalleerde pakket voldoet met de gegeven minimale versie:

`pacman -T "{{bash>=5}}"`

- Controleer of een latere versie van een pakket is geïnstalleerd:

`pacman -T "{{bash>5}}"`

- Toon de [h]elp:

`pacman -Th`
