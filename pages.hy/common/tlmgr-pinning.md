# tlmgr ամրացում

> Ամրացման գործողությունը կառավարում է ամրացման ֆայլը:.
> Լրացուցիչ տեղեկություններ. <https://www.tug.org/texlive/doc/tlmgr.html#pinning>:.

- Ցույց տալ ընթացիկ ամրացման տվյալները.:

`tlmgr pinning show`

- Փաթեթների համապատասխանեցումը ամրացրեք տվյալ պահեստին.:

`tlmgr pinning add {{repository}} {{package1 package2 ...}}`

- Հեռացրեք ցանկացած փաթեթ, որը գրանցված է կապող ֆայլում, որը համապատասխանում է տվյալ պահոցի փաթեթներին.:

`tlmgr pinning remove {{repository}} {{package1 package2 ...}}`

- Հեռացրեք բոլոր ամրացման տվյալները տվյալ պահոցի համար.:

`tlmgr pinning remove {{repository}} --all`
