# scalafmt

> Կոդերի ձևաչափիչ Scala-ի համար:.
> Կազմաձևերը պահվում են `.scalafmt.conf` ֆայլում:.
> Լրացուցիչ տեղեկություններ. <https://scalameta.org/scalafmt/>:.

- Վերափոխեք բոլոր `.scala` ֆայլերը ընթացիկ գրացուցակում ռեկուրսիվ կերպով.:

`scalafmt`

- Վերափոխեք հատուկ ֆայլեր կամ գրացուցակներ հատուկ ձևաչափման կազմաձևով.:

`scalafmt --config {{path/to/.scalafmt.conf}} {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Ստուգեք, արդյոք ֆայլերը ճիշտ ձևաչափված են, վերադարձնելով `0`, եթե բոլոր ֆայլերը համապատասխանում են ձևաչափման ոճին.:

`scalafmt --config {{path/to/.scalafmt.conf}} --test`

- Բացառել ֆայլերը կամ գրացուցակները.:

`scalafmt --exclude {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Ձևաչափեք միայն ֆայլերը, որոնք խմբագրվել են ընթացիկ Git ճյուղի համեմատ.:

`scalafmt --config {{path/to/.scalafmt.conf}} --mode diff`
