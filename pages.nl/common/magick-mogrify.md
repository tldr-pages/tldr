# magick mogrify

> Voer bewerkingen uit op meerdere afbeeldingen, zoals het wijzigen van de grootte, bijsnijden, omkeren en effecten toevoegen.
> Wijzigingen worden direct toegepast op het originele bestand.
> Bekijk ook: `magick`.
> Meer informatie: <https://imagemagick.org/script/mogrify.php>.

- Wijzig de grootte van alle JPEG afbeeldingen in de map naar 50% van hun oorspronkelijke grootte:

`magick mogrify -resize {{50%}} {{*.jpg}}`

- Wijzig de grootte van alle afbeeldingen die beginnen met `DSC` naar 800x600:

`magick mogrify -resize {{800x600}} {{DSC*}}`

- Converteer alle PNG's in de map naar JPEG:

`magick mogrify -format {{jpg}} {{*.png}}`

- Halveer de verzadiging van alle afbeeldingsbestanden in de huidige map:

`magick mogrify -modulate {{100,50}} {{*}}`

- Verdubbel de helderheid van alle afbeeldingsbestanden in de huidige map:

`magick mogrify -modulate {{200}} {{*}}`
