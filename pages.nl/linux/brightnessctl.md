# brightnessctl

> Hulpprogramma voor het uitlezen en besturen van de helderheid van apparaten voor Linux-besturingssystemen.
> Meer informatie: <https://github.com/Hummer12007/brightnessctl#usage>.

- Toon apparaten met aanpasbare helderheid:

`brightnessctl {{[-l|--list]}}`

- Toon de huidige helderheid van het standaardapparaat:

`brightnessctl {{[g|get]}}`

- Toon de huidige helderheid van een bepaald apparaat (kan een wildcard zijn):

`brightnessctl {{[g|get]}} {{[-d|--device]}} '{{apparaatnaam}}'`

- Stel de helderheid in op een bepaald percentage:

`brightnessctl {{[s|set]}} {{50}}%`

- Verhoog de helderheid met een bepaald percentage:

`brightnessctl {{[s|set]}} +{{10}}%`

- Verlaag de helderheid met een bepaald percentage:

`brightnessctl {{[s|set]}} {{10}}%-`
