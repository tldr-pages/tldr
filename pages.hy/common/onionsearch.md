# սոխի որոնում

> Քերեք URL-ները տարբեր `.onion` որոնման համակարգերում:.
> Նշում. `onionsearch`-ը պահանջում է Tor վստահված սերվեր, որն աշխատում է `localhost:9050`-ով; `.onion` կայքերն այցելելու համար անհրաժեշտ է Tor-ով միացված զննարկիչ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/megadose/OnionSearch#--usage>:.

- Պահանջեք արդյունքներ բոլոր որոնման համակարգերից.:

`onionsearch "{{string}}"`

- Հայցեք որոնման արդյունքներ հատուկ որոնման համակարգերից.:

`onionsearch "{{string}}" --engines {{tor66|deeplink|phobos|...}}`

- Որոնելիս բացառել որոշակի որոնման համակարգեր.:

`onionsearch "{{string}}" --exclude {{candle|ahmia|...}}`

- Սահմանափակեք յուրաքանչյուր շարժիչի համար բեռնվող էջերի քանակը.:

`onionsearch "{{stuxnet}}" --engines {{tor66|deeplink|phobos|...}} --limit {{3}}`

- Թվարկեք բոլոր աջակցվող որոնման համակարգերը.:

`onionsearch --help | grep {{[-A|--after-context]}} 1 {{[-i|--ignore-case]}} "supported engines"`
