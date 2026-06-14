# mvn գաղափար

> Ստեղծեք IntelliJ IDEA նախագծի ֆայլեր (`.ipr`, `.iml` և `.iws`) Maven նախագծի համար:.
> Նշում. այս փլագինը հեռացված է: Այն այլեւս չի պահպանվում։
> Լրացուցիչ տեղեկություններ. <https://maven.apache.org/plugins/maven-idea-plugin/usage.html>:.

- Ստեղծեք IntelliJ IDEA նախագծի բոլոր ֆայլերը.:

`mvn idea:idea`

- Ստեղծեք միայն նախագծի (`.ipr`) ֆայլը՝:

`mvn idea:project`

- Ստեղծեք միայն աշխատանքային տարածքի (`.iws`) ֆայլը՝:

`mvn idea:workspace`

- Ստեղծեք միայն մոդուլի (`.iml`) ֆայլեր.:

`mvn idea:module`

- Ջնջել բոլոր ստեղծված նախագծի ֆայլերը.:

`mvn idea:clean`
