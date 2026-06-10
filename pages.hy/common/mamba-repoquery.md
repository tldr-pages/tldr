# mamba repoquery

> Արդյունավետ հարցումներ կատարեք conda-ի և mamba-ի փաթեթների պահոցների և փաթեթների կախվածության վերաբերյալ:.
> Լրացուցիչ տեղեկություններ. <https://mamba.readthedocs.io/en/latest/user_guide/mamba.html#repoquery>:.

- Որոնեք որոշակի փաթեթի բոլոր հասանելի տարբերակները.:

`mamba repoquery search {{package}}`

- Որոնեք հատուկ սահմանափակումներ բավարարող բոլոր փաթեթները.:

`mamba repoquery search "{{sphinx<5}}"`

- Թվարկեք ներկայումս ակտիվացված միջավայրում տեղադրված փաթեթի կախվածությունները ծառի ձևաչափով.:

`mamba repoquery depends {{[-t|--tree]}} {{scipy}}`

- Տպեք փաթեթներ ընթացիկ միջավայրում, որոնք պահանջում են որոշակի փաթեթի տեղադրում (այսինքն՝ `depends`-ի հակառակը).:

`mamba repoquery whoneeds {{ipython}}`
