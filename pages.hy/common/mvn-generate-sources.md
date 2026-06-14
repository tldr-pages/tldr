# mvn առաջացնում-աղբյուրներ

> Ստեղծեք Maven նախագծի սկզբնական կոդը մինչև հիմնական կազմման փուլը:.
> Այս փուլն աշխատում է `initialize`-ից հետո և `process-sources`-ից առաջ:.
> Լրացուցիչ տեղեկություններ. <https://manned.org/mvn>:.

- Գործարկել կյանքի ցիկլի բոլոր փուլերը մինչև `generate-sources`:

`mvn generate-sources`

- Գործարկել հաջորդ փուլը՝ ռեսուրսներ ստեղծելու համար.:

`mvn generate-resources`

- Մաքրել և վերականգնել աղբյուրները.:

`mvn clean generate-sources`
