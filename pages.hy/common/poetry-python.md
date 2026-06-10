# պոեզիա-պիթոն

> Կառավարեք Python-ի տարբերակները պոեզիայի միջոցով:.
> Տես նաև՝ `asdf`:.
> Լրացուցիչ տեղեկություններ. <https://python-poetry.org/docs/cli/#python>:.

- Տեղադրեք նշված Python տարբերակը.:

`poetry python install {{3.13.1}}`

- Թվարկեք Python-ի բոլոր տարբերակները, որոնք կառավարվում են System-ի կամ Poetry-ի կողմից.:

`poetry python list`

- Թվարկեք Python-ի բոլոր տարբերակները, որոնք կառավարվում են Poetry-ի կողմից.:

`poetry python list --managed`

- Հեռացրեք Python-ի նշված տարբերակը (եթե կառավարվում է Poetry-ի կողմից).:

`poetry python remove {{3.13.1}}`
