# duc

> Een verzameling van tools voor het indexeren, inspecteren en visualiseren van schijfgebruik.
> Duc onderhoudt een database van geaccumuleerde groottes van directories van het bestandssysteem, waardoor je deze database kunt raadplegen of mooie grafieken kunt maken om te laten zien waar de data zich bevindt.
> Meer informatie: <https://htmlpreview.github.io/?https://github.com/zevv/duc/blob/master/doc/duc.1.html>.

- Indexeer de `/usr` directory en schrijf naar de standaard database locatie ~/.duc.db:

`duc index {{/usr}}`

- Toon alle bestanden en directories onder `/usr/local` en toon relatieve bestandsgroottes in een grafiek:

`duc ls {{[-Fg|--classify --graph]}} {{/usr/local}}`

- Toon alle bestanden en directories onder `/usr/local` recursief met behulp van boomweergave:

`duc ls {{[-Fg|--classify --graph]}} {{[-R|--recursive]}} {{/usr/local}}`

- Start de grafische interface om het bestandssysteem te verkennen met behulp van zonnestraalgrafieken:

`duc gui {{/usr}}`

- Start de ncurses console interface om het bestandssysteem te verkennen:

`duc ui {{/usr}}`

- Dump database-informatie:

`duc info`
