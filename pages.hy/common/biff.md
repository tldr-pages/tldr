#բիֆ

> Պարզ գործիք՝ ամսաթվերի թվաբանություն, վերլուծություն և ձևաչափում կատարելու համար:.
> Լրացուցիչ տեղեկություններ. <https://github.com/burntsushi/biff>:.

- Տպեք ընթացիկ ժամանակը ձեր ընտրած ձևաչափով.:

`biff time fmt {{[-f|--format]}} rfc3339 now`

- Տպել մի քանի հարաբերական անգամ մեկ հրամանով.:

`biff time fmt {{[-f|--format]}} '%c' now -1d 'next sat' 'last monday' '9pm last mon'`

- Տպեք ընթացիկ ժամը մեկ այլ ժամային գոտում և կլորացրեք այն մոտակա 15 րոպեի չափով.:

`biff time in Asia/Bangkok now | biff time round {{[-i|--increment]}} 15 {{[-s|--smallest]}} minute`

- Փոխարկել ժամանակը երկու տարբեր ժամային գոտիների միջև.:

`TZ='Japan' biff time in America/New_York 02:30`

- Տպել անցյալ կամ ապագա ժամանակը ընթացիկ ժամանակի համեմատ.:

`biff time add {{-1d|1d|1w|-1m|1y|...}} now`

- Ընթացիկ ժամանակին ավելացրեք բարդ տեւողություն.:

`biff time add '1 week, 12 hours ago' now`

- Գտեք տեւողությունը անցյալի ամսաթվից հետո և կլորացրեք այն ցանկալի ճշգրտությամբ.:

`biff span since 2025-01-20T12:00 {{[-l|--largest]}} year`

- Գտեք ժամանակի դրոշմակնիքները գրանցամատյանում և վերափոխեք դրանք ձեր տեղական ժամանակով.:

`biff tag lines /tmp/access.log | biff time in system | biff time fmt {{[-f|--format]}} '%c' | head {{[-n|--lines]}} 3 | biff untag {{[-s|--substitute]}}`
