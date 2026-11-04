# apt-get

> Hulpprogramma voor pakketbeheer van Debian en Ubuntu.
> Zoek naar pakketten met `apt-cache`.
> Het is aanbevolen om `apt` te gebruiken wanneer het interactief wordt gebruikt in Ubuntu versies 16.04 en later.
> Meer informatie: <https://manned.org/apt-get.8>.

- Werk de lijst van beschikbare pakketten en versies bij (het wordt aanbevolen dit uit te voeren voor elk ander `apt-get` commando):

`sudo apt-get update`

- Installeer een pakket, of werk het bij naar de nieuwste beschikbare versie:

`sudo apt-get install {{pakket}}`

- Verwijder een pakket:

`sudo apt-get remove {{pakket}}`

- Verwijder een pakket en zijn configuratiebestanden:

`sudo apt-get purge {{pakket}}`

- Upgrade alle geïnstalleerde pakketten naar hun nieuwste beschikbare versies:

`sudo apt-get upgrade`

- Schoon de lokale repository op - verwijder pakketbestanden (`.deb`) van onderbroken downloads die niet langer kunnen worden gedownload:

`sudo apt-get autoclean`

- Verwijder alle pakketten die niet meer nodig zijn:

`sudo apt-get autoremove`

- Upgrade geïnstalleerde pakketten (zoals `upgrade`), maar verwijder verouderde pakketten en installeer aanvullende pakketten om aan nieuwe dependencies te voldoen:

`sudo apt-get dist-upgrade`
