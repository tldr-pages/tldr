# apt-get

> Hulpprogramma voor pakketbeheer van Debian en Ubuntu.
> Zoek naar pakketten met `apt-cache`.
> Meer informatie: <https://manpages.debian.org/latest/apt/apt-get.8.html>.

- Werk de lijst van beschikbare pakketten en versies bij (het wordt aanbevolen dit uit te voeren voor elk ander `apt-get` commando):

`apt-get update`

- Installeer of werk het pakket bij naar de laatste beschikbare versie:

`apt-get install {{package}}`

- Een pakket verwijderen:

`apt-get remove {{package}}`

- Verwijder een pakket en de bijbehorende configuratiebestanden:

`apt-get purge {{package}}`

- Upgrade alle geïnstalleerde pakketten naar hun nieuwste beschikbare versies:

`apt-get upgrade`

- Schoon de lokale repository op - verwijder pakketbestanden (`.deb`) van onderbroken downloads die niet langer kunnen worden gedownload:

`apt-get autoclean`

- Verwijder alle pakketten die niet meer nodig zijn:

`apt-get autoremove`

- Upgrade geïnstalleerde pakketten (zoals `upgrade`), maar verwijder verouderde pakketten en installeer aanvullende pakketten om aan nieuwe dependencies te voldoen:

`apt-get dist-upgrade`
