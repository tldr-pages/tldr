# kiterunner kb

> Համատեքստային վեբ սկաներ՝ API-ի և վեբ վերջնակետի հայտնաբերման մեջ օգտագործվող kitebuilder սխեմաների մանիպուլյացիայի համար:.
> `kb` ենթահրամանը կարգավորում է սխեմայի կազմումը, փոխարկումը, վերլուծությունը և կրկնակի խնդրանքը:.
> Լրացուցիչ տեղեկություններ. <https://github.com/assetnote/kiterunner#usage>:.

- Կազմեք kitebuilder սխեման JSON-ից դեպի kite ֆայլ.:

`kiterunner kb compile {{path/to/wordlist.json}} {{path/to/wordlist.kite}}`

- Վերափոխեք ուրուրի ֆայլը տեքստային բառերի ցանկի.:

`kiterunner kb convert {{path/to/wordlist.kite}} {{path/to/wordlist.txt}}`

- Տեքստային բառացանկը փոխարկեք ուրուրի ֆայլի.:

`kiterunner kb convert {{path/to/wordlist.txt}} {{path/to/wordlist.kite}}`

- Փոխարկեք kite ֆայլը JSON սխեմայի.:

`kiterunner kb convert {{path/to/wordlist.kite}} {{path/to/wordlist.json}}`

- Վերլուծեք kitebuilder-ի սխեման և թողարկեք բարելավված JSON տվյալներ.:

`kiterunner kb parse {{path/to/wordlist.json}} {{[-o|--output]}} {{json}}`

- Վերլուծեք ուրուրի ֆայլը և թողարկեք տեքստային հստակ տվյալներ.:

`kiterunner kb parse {{path/to/wordlist.kite}} {{[-o|--output]}} {{text}}`

- Կրկնել հատուկ հարցումը kitebuilder սխեմայի ելքից.:

`kiterunner kb replay {{[-w|--kitebuilder-list]}} {{path/to/wordlist.kite}} "{{request_output}}"`

- Կրկնել հարցումը վստահված անձի միջոցով ստուգման համար.:

`kiterunner kb replay {{[-w|--kitebuilder-list]}} {{path/to/wordlist.kite}} {{[-p|--proxy]}} {{http://localhost:8080}} "{{request_output}}"`
