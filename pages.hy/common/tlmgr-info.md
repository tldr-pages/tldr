# tlmgr տեղեկատվություն

> Ցույց տալ տեղեկատվություն TeX Live փաթեթների մասին:.
> Լրացուցիչ տեղեկություններ. <https://www.tug.org/texlive/doc/tlmgr.html#info>:.

- Թվարկեք բոլոր հասանելի TeX Live փաթեթները՝ նախադասելով տեղադրվածները `i`-ով:

`tlmgr info`

- Թվարկեք բոլոր հասանելի հավաքածուները.:

`tlmgr info collections`

- Թվարկեք բոլոր առկա սխեմաները.:

`tlmgr info scheme`

- Ցույց տալ տեղեկատվություն կոնկրետ փաթեթի մասին.:

`tlmgr info {{package}}`

- Թվարկեք բոլոր ֆայլերը, որոնք պարունակվում են որոշակի փաթեթում.:

`tlmgr info {{package}} --list`

- Նշեք բոլոր տեղադրված փաթեթները.:

`tlmgr info --only-installed`

- Ցույց տալ միայն կոնկրետ տեղեկատվություն փաթեթի մասին.:

`tlmgr info {{package}} --data "{{name}},{{category}},{{installed}},{{size}},{{depends}},{{...}}"`

- Տպեք բոլոր հասանելի փաթեթները որպես JSON կոդավորված զանգված.:

`tlmgr info --json`
