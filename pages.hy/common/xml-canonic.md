# xml կանոնական

> XML փաստաթղթերը կանոնական դարձրեք:.
> Լրացուցիչ տեղեկություններ. <https://xmlstar.sourceforge.net/doc/UG/xmlstarlet-ug.html#idm47077139560880>:.

- XML փաստաթուղթը դարձրեք կանոնական՝ պահպանելով մեկնաբանությունները.:

`xml {{[c14n|canonic]}} {{path/to/input.xml|uri}} > {{path/to/output.xml}}`

- XML փաստաթուղթը դարձրեք կանոնական՝ հեռացնելով մեկնաբանությունները.:

`xml {{[c14n|canonic]}} --without-comments {{path/to/input.xml|uri}} > {{path/to/output.xml}}`

- XML-ը դարձրեք բացառապես կանոնական՝ օգտագործելով XPATH ֆայլից՝ պահպանելով մեկնաբանությունները.:

`xml {{[c14n|canonic]}} --exc-with-comments {{path/to/input.xml|uri}} {{path/to/c14n.xpath}}`

- Ցուցադրել օգնությունը.:

`xml {{[c14n|canonic]}} --help`
