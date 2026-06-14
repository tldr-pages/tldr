# plesk

> Plesk հոստինգի կառավարման վահանակ:.
> Լրացուցիչ տեղեկություններ. <https://docs.plesk.com/en-US/obsidian/cli-linux/plesk-utility.75661/>:.

- Ստեղծեք ավտոմատ մուտքի հղում ադմինիստրատորի օգտագործողի համար և տպեք այն.:

`plesk login`

- Թվարկեք բոլոր հյուրընկալված տիրույթները.:

`plesk bin domain --list`

- Start watching for changes in the `panel.log` file:

`plesk log {{panel.log}}`

- Սկսեք ինտերակտիվ MySQL վահանակը.:

`plesk db`

- Բացեք Plesk հիմնական կազմաձևման ֆայլը լռելյայն խմբագրում.:

`plesk conf {{panel.ini}}`

- Ցուցադրման տարբերակը:

`plesk version`
