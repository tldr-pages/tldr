# clamdscan

> Սկանավորեք վիրուսների համար՝ օգտագործելով ClamAV Daemon:.
> Լրացուցիչ տեղեկություններ. <https://docs.clamav.net/manual/Usage/Scanning.html#clamdscan>:.

- Սկանավորեք ֆայլը կամ գրացուցակը խոցելիության համար.:

`clamdscan {{path/to/file_or_directory}}`

- Սկանավորեք տվյալները `stdin`-ից՝:

`{{command}} | clamdscan -`

- Սկանավորեք ընթացիկ գրացուցակը և թողարկեք միայն վարակված ֆայլերը.:

`clamdscan --infected`

- Տպեք սկանավորման հաշվետվությունը գրանցամատյանում.:

`clamdscan --log {{path/to/log_file}}`

- Վարակված ֆայլերը տեղափոխեք որոշակի գրացուցակ.:

`clamdscan --move {{path/to/quarantine_directory}}`

- Հեռացրեք վարակված ֆայլերը.:

`clamdscan --remove`

- Օգտագործեք բազմաթիվ թելեր՝ գրացուցակը սկանավորելու համար.:

`clamdscan --multiscan`

- Ֆայլը դեյմոնին փոխանցելու փոխարեն փոխանցեք ֆայլի նկարագրիչը.:

`clamdscan --fdpass`
