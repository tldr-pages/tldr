# pcdovtoppm

> Maak een indexafbeelding voor een fotocd op basis van het overzichtsbestand.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pcdovtoppm.html>.

- Maak een PPM-indexafbeelding van een PCD-overzichtsbestand:

`pcdovtoppm {{pad/naar/bestand.pcd}} > {{pad/naar/uitvoer.ppm}}`

- Specificeer de [m]aximale breedte van de uitvoer-afbeelding en de maximale grootte ([s]) van elke afbeelding die in de uitvoer wordt opgenomen:

`pcdovtoppm -m {{breedte}} -s {{grootte}} {{pad/naar/bestand.pcd}} > {{pad/naar/uitvoer.ppm}}`

- Specificeer het maximale [a]antal afbeeldingen en het maximale aantal kleuren ([c]):

`pcdovtoppm -a {{n_afbeeldingen}} -c {{n_kleuren}} {{pad/naar/bestand.pcd}} > {{pad/naar/uitvoer.ppm}}`

- Gebruik het gespecificeerde lettertype ([f]) voor annotaties en kleur de achtergrond [w]it:

`pcdovtoppm -f {{lettertype}} -w {{pad/naar/bestand.pcd}} > {{pad/naar/uitvoer.ppm}}`
