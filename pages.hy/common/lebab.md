#լեբաբ

> JavaScript-ի արդիականացուցիչ՝ կոդը ES6/ES7-ին փոխանցելու համար:.
> Բոլոր օրինակների համար պետք է տրամադրվեն փոխակերպումներ:.
> Լրացուցիչ տեղեկություններ. <https://github.com/lebab/lebab>:.

- Տրանսպիլ՝ օգտագործելով մեկ կամ մի քանի ստորակետերով բաժանված փոխակերպումներ.:

`lebab --transform {{transformation1,transformation2,...}}`

- Փոխանցել ֆայլը `stdout`՝:

`lebab {{path/to/input_file}}`

- Փոխանցել ֆայլը նշված ելքային ֆայլին.:

`lebab {{path/to/input_file}} --out-file {{path/to/output_file}}`

- Փոխարինեք բոլոր `.js` ֆայլերը տեղում նշված գրացուցակում, գլոբում կամ ֆայլում.:

`lebab --replace {{directory|glob|file}}`

- Ցուցադրել օգնությունը.:

`lebab --help`
