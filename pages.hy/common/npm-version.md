# npm տարբերակ

> Bump a node փաթեթի տարբերակը:.
> Լրացուցիչ տեղեկություններ. <https://docs.npmjs.com/cli/npm-version/>:.

- Ցուցադրման տարբերակը:

`npm version`

- Բացեք փոքր տարբերակը.:

`npm version minor`

- Սահմանեք հատուկ տարբերակ.:

`npm version {{version}}`

- Բացեք կարկատել տարբերակը՝ առանց Git թեգ ստեղծելու.:

`npm version patch --no-git-tag-version`

- Բացեք հիմնական տարբերակը հատուկ հաղորդագրությամբ.:

`npm version major {{[-m|--message]}} "{{Upgrade to %s for reasons}}"`
