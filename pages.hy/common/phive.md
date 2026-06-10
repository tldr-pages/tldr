#փիվի

> Phar-ի տեղադրման և ստուգման միջավայրը PHP հավելվածի անվտանգ տեղակայման համար:.
> Լրացուցիչ տեղեկություններ. <https://phar.io/#Usage>:.

- Ցուցադրել հասանելի կեղծանունով Phars-ների ցանկը.:

`phive list`

- Տեղադրեք նշված Phar-ը տեղական գրացուցակում.:

`phive install {{alias|url}}`

- Տեղադրեք նշված Phar-ը ամբողջ աշխարհում.:

`phive install {{alias|url}} {{[-g|--global]}}`

- Տեղադրեք նշված Phar-ը թիրախային գրացուցակում.:

`phive install {{alias|url}} {{[-t|--target]}} {{path/to/directory}}`

- Թարմացրեք բոլոր Phar ֆայլերը վերջին տարբերակին.:

`phive update`

- Հեռացրեք նշված Phar ֆայլը.:

`phive remove {{alias|url}}`

- Հեռացրեք չօգտագործված Phar ֆայլերը.:

`phive purge`

- Թվարկեք բոլոր հասանելի հրամանները.:

`phive help`
