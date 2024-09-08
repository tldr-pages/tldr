# duc

> Een verzameling tools voor het indexeren, inspecteren en visualiseren van schijfgebruik.
> Duc onderhoudt een database van geaccumuleerde groottes van directories in het bestandssysteem, waardoor je deze database kunt raadplegen of mooie grafieken kunt maken om te laten zien waar de data zich bevindt.
> Meer informatie: <https://duc.zevv.nl/>.

- Indexeer de `/usr` directory en schrijf naar de standaard database locatie `~/.duc.db`:

`duc index {{/usr}}`

- Lijst alle bestanden en directories onder `/usr/local` en toon relatieve bestandsgroottes in een [g]rafiek:

`duc ls --classify --graph {{/usr/local}}`

- Lijst alle bestanden en directories onder `/usr/local` recursief met behulp van boomweergave:

`duc ls --classify --graph --recursive {{/usr/local}}`

- Start de grafische interface om het bestandssysteem te verkennen met behulp van zonnestraalgrafieken:

`duc gui {{/usr}}`

- Start de ncurses console interface om het bestandssysteem te verkennen:

`duc ui {{/usr}}`

- Dump database-informatie:

`duc info`
