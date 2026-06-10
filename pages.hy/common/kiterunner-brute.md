# kiterunner brute

> Համատեքստային վեբ սկաներ՝ բառացանկերի միջոցով API-ի ուղիների և վեբ վերջնակետերի կոպիտ ուժի համար:.
> `brute` ենթահրամանը թիրախավորում է մեկ կամ մի քանի սերվեր:.
> Լրացուցիչ տեղեկություններ. <https://github.com/assetnote/kiterunner#usage>:.

- Bruteforce թիրախը Assetnote բառացանկով (օրինակ՝ առաջին 20,000 API երթուղիները).:

`kiterunner brute {{https://example.com}} {{[-A|--assetnote-wordlist]}} {{apiroutes-210328:20000}}`

- Bruteforce թիրախը հատուկ բառացանկով.:

`kiterunner brute {{https://example.com}} {{[-w|--wordlist]}} {{path/to/wordlist.txt}}`

- Bruteforce՝ օգտագործելով dirsearch ոճով բառացանկ՝ ընդարձակման փոխարինմամբ.:

`kiterunner brute {{https://example.com}} {{[-w|--wordlist]}} {{path/to/dirsearch.txt}} {{[-D|--dirsearch-compat]}} {{[-e|--extensions]}} {{json,txt}}`

- Bruteforce հատուկ ֆայլերի ընդարձակմամբ կցված և JSON ձևաչափով թողարկված.:

`kiterunner brute {{https://example.com}} {{[-w|--wordlist]}} {{path/to/wordlist.txt}} {{[-e|--extensions]}} {{aspx,ashx}} {{[-o|--output]}} {{json}}`

- Bruteforce թիրախների ցանկը ֆայլից, որն ունի հատուկ համաժամանակյա կարգավորումներ կատարման համար.:

`kiterunner brute {{path/to/targets.txt}} {{[-w|--wordlist]}} {{path/to/wordlist.txt}} {{[-x|--max-connection-per-host]}} {{5}} {{[-j|--max-parallel-hosts]}} {{100}}`

- Bruteforce և անտեսեք կոնկրետ բովանդակության երկարության պատասխանները.:

`kiterunner brute {{https://example.com}} {{[-w|--wordlist]}} {{path/to/wordlist.txt}} --ignore-length {{100-105}}`

- Bruteforce հատուկ HTTP վերնագրերով.:

`kiterunner brute {{https://example.com}} {{[-w|--wordlist]}} {{path/to/wordlist.txt}} {{[-H|--header]}} "{{Authorization: Bearer token}}"`

- Bruteforce թիրախների ցանկը ֆայլից ձախողման կարգավիճակի կոդի զտիչով.:

`kiterunner brute {{path/to/targets.txt}} {{[-w|--wordlist]}} {{path/to/wordlist.txt}} --fail-status-codes {{400,401,404}}`
