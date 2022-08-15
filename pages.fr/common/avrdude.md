# avrdude

> Pilotes pour programmer les microcontrôleurs Atmel AVR.
> Plus d'informations : <https://www.nongnu.org/avrdude/>.

- Lire le contenu du microcontrôleur AVR :

`avrdude -p {{appareil_AVR}} -c {{programmeur}} -U flash:r:{{fichier.hex}}:i`

- Programme le microcontrôleur AVR :

`avrdude -p {{appareil_AVR}} -c {{programmeur}} -U flash:w:{{fichier.hex}}`

- Affiche les appareils AVR disponibles :

`avrdude -p \?`

- Affiche les programmeurs AVR disponibles :

`avrdude -c \?`
