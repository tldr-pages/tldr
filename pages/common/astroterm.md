# astroterm

> A terminal-based star map.
> More information: <https://github.com/da-luce/astroterm>.

- Display real-time positions of stars and planets based on your current location:

`astroterm`

- Display constellations, use colour, and render the simulation at the given frame rate:

`astroterm --constellations --color --fps={{60}}`

- Use unicode characters instead of the basic ASCII characters, and only render stars brighter than the given magnitude:

`astroterm --unicode --threshold={{2.0}}`

- Use a given latitude, longitude and datetime:

`astroterm --latitude={{90.0}} --longitude={{-180.0}} --datetime={{2025-08-04T12:00:00}}`

- Use the longitude and latitude of a given city, and set the speed of the simulation to a given factor:

`astroterm --city={{Singapore}} --speed={{1000.0}}`
