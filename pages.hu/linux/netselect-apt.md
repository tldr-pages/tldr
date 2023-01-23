# netselect-apt

> Hozzon létre egy `sources.list` fájlt a legalacsonyabb késleltetésű Debian-tükör számára. További információ: <https://manpages.debian.org/latest/netselect-apt/netselect-apt.html>.

- Hozzon létre `sources.list` a legalacsonyabb késleltetésű szerver használatával:

`sudo netselect-apt`

- Adja meg a Debian ágat, alapértelmezés szerint a stable-t használja:

`sudo netselect-apt {{testing}}`

- Bele kell foglalni a non-free szakaszt:

`sudo netselect-apt --non-free`

- Adjon meg egy országot a tükörlista kereséséhez:

`sudo netselect-apt -c {{India}}`
