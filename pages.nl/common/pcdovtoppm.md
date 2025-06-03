# pcdovtoppm

> Maak een indexafbeelding voor een fotocd op basis van het overzichtsbestand.
> Meer informatie: <https://netpbm.sourceforge.net/doc/pcdovtoppm.html>.

- Maak een PPM-indexafbeelding van een PCD-overzichtsbestand:

`pcdovtoppm {{pad/naar/bestand.pcd}} > {{pad/naar/uitvoer.ppm}}`

- Specificeer de maximale breedte van de uitvoer-afbeelding en de maximale grootte van elke afbeelding die in de uitvoer wordt opgenomen:

`pcdovtoppm {{[-m|-maxwidth]}} {{breedte}} {{[-s|-size]}} {{grootte}} {{pad/naar/bestand.pcd}} > {{pad/naar/uitvoer.ppm}}`

- Specificeer het maximale aantal afbeeldingen en het maximale aantal kleuren:

`pcdovtoppm {{[-a|-across]}} {{n_afbeeldingen}} {{[-c|-colors]}} {{n_kleuren}} {{pad/naar/bestand.pcd}} > {{pad/naar/uitvoer.ppm}}`

- Gebruik het gespecificeerde lettertype voor annotaties en kleur de achtergrond wit:

`pcdovtoppm {{[-f|-font]}} {{lettertype}} {{[-w|-white]}} {{pad/naar/bestand.pcd}} > {{pad/naar/uitvoer.ppm}}`
