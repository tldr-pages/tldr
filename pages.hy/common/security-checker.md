# անվտանգության ստուգիչ

> Ստուգեք՝ արդյոք PHP հավելվածն օգտագործում է կախվածություն՝ հայտնի անվտանգության խոցելիություններով:.
> Լրացուցիչ տեղեկություններ. <https://github.com/sensiolabs/security-checker>:.

- Անվտանգության խնդիրներ փնտրեք նախագծի կախվածության մեջ (հիմնվելով ընթացիկ գրացուցակի `composer.lock` ֆայլի վրա).:

`security-checker security:check`

- Օգտագործեք որոշակի `composer.lock` ֆայլ՝:

`security-checker security:check {{path/to/composer.lock}}`

- Վերադարձեք արդյունքները որպես JSON օբյեկտ.:

`security-checker security:check --format=json`
