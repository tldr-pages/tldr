# dolt ճյուղ

> Կառավարեք Dolt մասնաճյուղերը:.
> Լրացուցիչ տեղեկություններ. <https://docs.dolthub.com/cli-reference/cli#dolt-branch>:.

- Ցուցակեք տեղական մասնաճյուղերը (ընթացիկ մասնաճյուղը ընդգծված է `*`-ով):

`dolt branch`

- Թվարկեք բոլոր տեղական և հեռավոր մասնաճյուղերը.:

`dolt branch {{[-A|--all]}}`

- Ստեղծեք նոր մասնաճյուղ ընթացիկ մասնաճյուղի հիման վրա.:

`dolt branch {{branch_name}}`

- Ստեղծեք նոր մասնաճյուղ՝ նշված commit-ով որպես վերջին՝:

`dolt branch {{branch_name}} {{commit}}`

- Վերանվանել մասնաճյուղը.:

`dolt branch {{[-m|--move]}} {{branch_name1}} {{branch_name2}}`

- Կրկնօրինակեք մասնաճյուղը.:

`dolt branch {{[-c|--copy]}} {{branch_name1}} {{branch_name2}}`

- Ջնջել մասնաճյուղը.:

`dolt branch {{[-d|--delete]}} {{branch_name}}`

- Ցուցադրել ընթացիկ մասնաճյուղի անունը.:

`dolt branch --show-current`
