# msgattrib

> Զտել և շահարկել հաղորդագրության հատկանիշները `.po` թարգմանական ֆայլերում:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/gettext/manual/gettext.html#msgattrib-Invocation>:.

- Պահպանեք միայն թարգմանված հաղորդագրությունները.:

`msgattrib --translated {{input.po}} > {{translated.po}}`

- Պահպանեք միայն չթարգմանված հաղորդագրությունները.:

`msgattrib --untranslated {{input.po}} > {{untranslated.po}}`

- Հեռացրեք անորոշ հաղորդագրությունները.:

`msgattrib --no-fuzzy {{input.po}} > {{clean.po}}`

- Պահպանեք միայն անորոշ հաղորդագրություններ.:

`msgattrib --only-fuzzy {{input.po}} > {{fuzzy.po}}`

- Նշեք բոլոր հաղորդագրությունները որպես մշուշոտ.:

`msgattrib --set-fuzzy {{input.po}} > {{fuzzy.po}}`

- Մաքրել մշուշոտ նշանները.:

`msgattrib --clear-fuzzy {{input.po}} > {{clean.po}}`

- Տեսակավորել արտադրանքը ըստ ֆայլի գտնվելու վայրի.:

`msgattrib {{[-F|--sort-by-file]}} {{input.po}} > {{sorted.po}}`

- Ցուցադրել օգնությունը.:

`msgattrib {{[-h|--help]}}`
