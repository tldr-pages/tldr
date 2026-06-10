# կակղամորթ

> Վիրուսի սկաներ:.
> Լրացուցիչ տեղեկություններ. <https://docs.clamav.net/manual/Usage/Scanning.html#clamscan>:.

- Սկանավորեք ֆայլը խոցելիության համար.:

`clamscan {{path/to/file}}`

- Սկանավորեք բոլոր ֆայլերը ռեկուրսիվորեն որոշակի գրացուցակում.:

`clamscan {{[-r|--recursive]}} {{path/to/directory}}`

- Տվյալների սկանավորում `stdin`-ից՝:

`{{command}} | clamscan -`

- Նշեք վիրուսների տվյալների բազայի ֆայլը կամ ֆայլերի գրացուցակը.:

`clamscan {{[-d|--database]}} {{path/to/database_file_or_directory}}`

- Սկանավորեք ընթացիկ գրացուցակը և թողարկեք միայն վարակված ֆայլերը.:

`clamscan {{[-i|--infected]}}`

- Տպեք սկանավորման հաշվետվությունը գրանցամատյանում.:

`clamscan {{[-l|--log]}} {{path/to/log_file}}`

- Վարակված ֆայլերը տեղափոխեք որոշակի գրացուցակ.:

`clamscan --move {{path/to/quarantine_directory}}`

- Հեռացրեք վարակված ֆայլերը.:

`clamscan --remove yes`
