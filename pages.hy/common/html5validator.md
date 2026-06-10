# html5 վավերացնող

> Վավերացնել HTML5-ը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/svenkreiss/html5validator>:.

- Վավերացրեք որոշակի ֆայլ.:

`html5validator {{path/to/file}}`

- Վավերացրեք բոլոր HTML ֆայլերը որոշակի գրացուցակում.:

`html5validator --root {{path/to/directory}}`

- Ցույց տալ նախազգուշացումները, ինչպես նաև սխալները.:

`html5validator --show-warnings {{path/to/file}}`

- Համապատասխանեցրեք բազմաթիվ ֆայլեր՝ օգտագործելով գլոբալ օրինաչափություն.:

`html5validator --root {{path/to/directory}} --match "{{*.html *.php}}"`

- Անտեսեք հատուկ գրացուցակների անունները.:

`html5validator --root {{path/to/directory}} --blacklist "{{node_modules vendor}}"`

- Արդյունքները թողարկեք հատուկ ձևաչափով.:

`html5validator --format {{gnu|xml|json|text}} {{path/to/file}}`

- Արտադրեք գրանցամատյանը հատուկ խոսակցական մակարդակով.:

`html5validator --root {{path/to/directory}} --log {{debug|info|warning}}`
