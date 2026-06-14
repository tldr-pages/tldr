# kiterunner սկան

> Համատեքստային վեբ սկաներ API-ի ուղիները և վեբ վերջնակետերը միաժամանակ սկանավորելու համար՝ օգտագործելով kitebuilder բառացանկերը:.
> `scan` ենթահրամանը թիրախավորում է API-ի կառուցվածքային հարցումներով մեկ կամ մի քանի հոսթ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/assetnote/kiterunner#usage>:.

- Սկանավորեք թիրախը Assetnote բառացանկով (օրինակ՝ առաջին 5000 API երթուղիները).:

`kiterunner scan {{https://example.com}} {{[-A|--assetnote-wordlist]}} {{apiroutes-210228:5000}}`

- Սկանավորեք թիրախը kitebuilder բառացանկով.:

`kiterunner scan {{https://example.com}} {{[-w|--kitebuilder-list]}} {{path/to/wordlist.kite}}`

- Սկանավորեք բազմաթիվ հյուրընկալողներ ֆայլից kitebuilder բառացանկով.:

`kiterunner scan {{path/to/hosts.txt}} {{[-w|--kitebuilder-list]}} {{path/to/wordlist.kite}}`

- Սկանավորեք Assetnote բառացանկով և JSON ելքով.:

`kiterunner scan {{https://example.com}} {{[-A|--assetnote-wordlist]}} {{apiroutes-210228:5000}} -o {{json}}`

- Կատարման համար սկանավորեք համաժամանակյա պարամետրերով.:

`kiterunner scan {{https://example.com}} {{[-w|--kitebuilder-list]}} {{path/to/wordlist.kite}} {{[-x|--max-connection-per-host]}} {{5}} {{[-j|--max-parallel-hosts]}} {{100}}`

- Սկանավորեք բառացանկով որպես սովորական բառացանկ՝ անջատելով խորության սկանավորումը.:

`kiterunner scan {{https://example.com}} {{[-w|--kitebuilder-list]}} {{path/to/rafter.txt}} {{[-d|--preflight-depth]}} {{0}}`

- Սկանավորեք հատուկ վերնագրերով և անտեսեք կոնկրետ բովանդակության երկարության պատասխանները.:

`kiterunner scan {{https://example.com}} {{[-w|--kitebuilder-list]}} {{path/to/wordlist.kite}} {{[-H|--header]}} "{{Authorization: Bearer token}}" --ignore-length {{100-105}}`

- Կատարել ամբողջական kitebuilder սկան առանց փուլային սկանավորման.:

`kiterunner scan {{https://example.com}} {{[-w|--kitebuilder-list]}} {{path/to/wordlist.kite}} --kitebuilder-full-scan`
