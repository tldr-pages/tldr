# dnf download

> Download RPM-pakketten uit de DNF-repositories.
> Niet standaard inbegrepen bij `dnf`, maar ondersteund via `dnf-plugins-core`.
> Zie ook: `dnf`.
> Meer informatie: <https://dnf-plugins-core.readthedocs.io/en/latest/download.html>.

- Download de recentste versie van een pakket naar de huidige map:

`dnf download {{pakket}}`

- Download een pakket naar een specifieke map (de map moet bestaan):

`dnf download {{pakket}} --destdir {{pad/naar/map}}`

- Toon de URL waar het RPM-pakket kan worden gedownload:

`dnf download --url {{pakket}}`
