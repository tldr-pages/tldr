# kiterunner բառացանկ

> Համատեքստային վեբ սկաներ՝ API-ի և վեբ վերջնակետի հայտնաբերման մեջ օգտագործվող բառացանկերի կառավարման համար:.
> `wordlist` ենթահրամանը կարգավորում և պահպանում է բառերի ցուցակները `~/.cache/kiterunner`-ում:.
> Լրացուցիչ տեղեկություններ. <https://github.com/assetnote/kiterunner#usage>:.

- Թվարկեք բոլոր պահված և հասանելի Assetnote բառացանկերը.:

`kiterunner wordlist list`

- Ցուցակեք բառացանկերը JSON ելքով.:

`kiterunner wordlist list {{[-o|--output]}} {{json}}`

- Թվարկեք բառացանկերը, որոնք ունեն վրիպազերծման ծավալուն արդյունք.:

`kiterunner wordlist list {{[-v|--verbose]}} {{debug}}`

- Պահպանեք հատուկ Assetnote բառացանկը կեղծանունով.:

`kiterunner wordlist save {{apiroutes-210328}}`

- Պահպանեք հատուկ Assetnote բառացանկը լրիվ ֆայլի անունով.:

`kiterunner wordlist save {{path/to/httparchive_apiroutes_2024_05_28.txt}}`

- Պահպանեք բազմաթիվ բառացանկեր ըստ կեղծանունների.:

`kiterunner wordlist save {{apiroutes-210328,aspx-210328}}`

- Պահպանեք բառացանկը հանգիստ ռեժիմով` ելքը ճնշելու համար.:

`kiterunner wordlist save {{apiroutes-210328}} {{[-q|--quiet]}}`
