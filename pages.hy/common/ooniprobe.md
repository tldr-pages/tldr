# ooniprobe

> Ցանցային միջամտության բաց աստղադիտարանը (OONI):.
> Փորձարկեք կայքերի և հավելվածների արգելափակումը: Չափեք ձեր ցանցի արագությունն ու կատարումը:.
> Լրացուցիչ տեղեկություններ. <https://ooni.org/support/ooni-probe-cli/>:.

- Թվարկեք կատարված բոլոր թեստերը.:

`ooniprobe list`

- Ցույց տալ տեղեկատվություն կոնկրետ թեստի մասին.:

`ooniprobe list {{7}}`

- Գործարկել բոլոր առկա թեստերը.:

`ooniprobe run all`

- Կատարել հատուկ թեստ.:

`ooniprobe run {{performance}}`

- Ստուգեք կոնկրետ կայքի առկայությունը.:

`ooniprobe run websites --input {{https://ooni.org/}}`

- Ստուգեք ֆայլում թվարկված բոլոր կայքերի առկայությունը.:

`ooniprobe run websites --input-file {{path/to/my-websites.txt}}`

- Ցուցադրել մանրամասն տեղեկատվություն թեստի մասին JSON ձևաչափով.:

`ooniprobe show {{9}}`
