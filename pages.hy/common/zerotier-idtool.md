# zerotier-idtool

> Ստեղծեք և շահարկեք ZeroTier ինքնությունները:.
> Տես նաև՝ `zerotier-cli`, `zerotier-one`:.
> Լրացուցիչ տեղեկություններ. <https://github.com/zerotier/ZeroTierOne/blob/dev/doc/zerotier-idtool.1.md>:.

- Ստեղծեք նոր ZeroTier ինքնություն և թողարկեք գաղտնի մասը `stdout`:

`zerotier-idtool generate`

- Ստեղծեք նոր ZeroTier ինքնություն և պահեք գաղտնի և հանրային մասերը ֆայլերում.:

`zerotier-idtool generate {{path/to/identity.secret}} {{path/to/identity.public}}`

- Ստեղծեք նոր ZeroTier ինքնություն հատուկ տասնվեցական ունայնության նախածանցով (կարող է երկար տևել).:

`zerotier-idtool generate {{path/to/identity.secret}} {{path/to/identity.public}} {{vanity_prefix}}`

- հանեք հանրային մասը գաղտնի ինքնությունից.:

`zerotier-idtool getpublic {{path/to/identity.secret}}`

- Ստորագրեք ֆայլ՝ օգտագործելով գաղտնի ինքնությունը.:

`zerotier-idtool sign {{path/to/identity.secret}} {{path/to/file}}`

- Ստուգեք ստորագրված ֆայլը՝ օգտագործելով հանրային ինքնությունը և տասնվեցական ստորագրությունը.:

`zerotier-idtool verify {{path/to/identity.public}} {{path/to/file}} {{signature_hex}}`

- Տեղայնորեն հաստատեք ինքնության բանալին և աշխատանքի ապացույցը.:

`zerotier-idtool validate {{path/to/identity.public}}`

- Ցուցադրել օգնությունը.:

`zerotier-idtool help`
