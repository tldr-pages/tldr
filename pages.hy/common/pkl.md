# pkl

> Կառավարեք, գնահատեք և փորձարկեք Pkl կազմաձևման մոդուլները:.
> Լրացուցիչ տեղեկություններ. <https://pkl-lang.org/main/current/pkl-cli/>:.

- Գնահատեք տրված Pkl մոդուլները և ստացեք դրանց մատուցման արդյունքները.:

`pkl eval {{module.pkl}}`

- Գործարկեք որպես սերվեր, որը հաղորդակցվում է `stdin`-ով և `stdout`-ով:

`pkl server`

- Գնահատեք Pkl մոդուլները որպես թեստեր և պատրաստեք հաշվետվություն.:

`pkl test {{module.pkl}}`

- Սկսեք REPL նստաշրջան.:

`pkl repl`

- Պատրաստեք Pkl նախագիծ՝ որպես փաթեթ հրատարակելու համար.:

`pkl project package {{path/to/project_directory}}`

- Լուծեք նախագծի կախվածությունները և լուծված տարբերակները գրում է ֆայլում `PklProject.deps.json` ճանապարհով:

`pkl project resolve {{path/to/project_directory}}`
