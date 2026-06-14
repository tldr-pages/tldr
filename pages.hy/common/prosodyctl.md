# prosodyctl

> Prosody XMPP սերվերի կառավարման գործիք:.
> Նշում. `prosodyctl`-ի միջոցով գործընթացի կառավարումը չի խրախուսվում: Փոխարենը, օգտագործեք ձեր համակարգի տրամադրած գործիքները (օրինակ՝ `systemctl`):.
> Լրացուցիչ տեղեկություններ. <https://prosody.im/doc/prosodyctl>:.

- Ցույց տալ Prosody սերվերի կարգավիճակը.:

`sudo prosodyctl status`

- Վերբեռնեք սերվերի կազմաձևման ֆայլերը.:

`sudo prosodyctl reload`

- Ավելացրեք օգտվող Prosody XMPP սերվերին.:

`sudo prosodyctl adduser {{user@example.com}}`

- Սահմանեք օգտվողի գաղտնաբառը.:

`sudo prosodyctl passwd {{user@example.com}}`

- Ընդմիշտ ջնջել օգտվողին.:

`sudo prosodyctl deluser {{user@example.com}}`
