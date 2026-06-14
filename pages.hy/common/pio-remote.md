# pio հեռակառավարման վահանակ

> Օգնական հրաման PlatformIO Remote Development-ի համար:.
> `pio remote [command]`-ն ընդունում է նույն արգումենտները, ինչ իր տեղական կատարող գործընկերը՝ `pio [command]`:.
> Լրացուցիչ տեղեկություններ. <https://docs.platformio.org/en/latest/core/userguide/remote/index.html>:.

- Թվարկեք բոլոր ակտիվ հեռավոր գործակալները.:

`pio remote agent list`

- Սկսեք նոր հեռակառավարման գործակալ հատուկ անունով և այն կիսեք ընկերների հետ.:

`pio remote agent start {{[-n|--name]}} {{agent_name}} {{[-s|--share]}} {{example1@example.com}} {{[-s|--share]}} {{example2@example.com}}`

- Նշեք սարքերը նշված գործակալներից (բաց թողեք `--agent`՝ բոլոր գործակալները նշելու համար).:

`pio remote --agent {{agent_name1}} --agent {{agent_name2}} device list`

- Միացեք հեռավոր սարքի սերիական պորտին.:

`pio remote --agent {{agent_name}} device monitor`

- Գործարկել բոլոր թիրախները նշված գործակալի վրա.:

`pio remote --agent {{agent_name}} run`

- Թարմացրեք տեղադրված հիմնական փաթեթները, զարգացման հարթակները և գլոբալ գրադարանները որոշակի գործակալի վրա.:

`pio remote --agent {{agent_name}} update`

- Գործարկեք բոլոր թեստերը բոլոր միջավայրերում որոշակի գործակալի վրա.:

`pio remote --agent {{agent_name}} test`
