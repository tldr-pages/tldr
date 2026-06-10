# wget

> Ներբեռնեք ֆայլերը համացանցից:.
> Աջակցում է HTTP, HTTPS և FTP:.
> Տես նաև՝ `wcurl`, `curl`:.
> Լրացուցիչ տեղեկություններ. <https://www.gnu.org/software/wget/manual/wget.html>:.

- Ներբեռնեք URL-ի բովանդակությունը ֆայլում (այս դեպքում կոչվում է «foo»).:

`wget {{https://example.com/foo}}`

- Ներբեռնեք URL-ի բովանդակությունը ֆայլում (այս դեպքում կոչվում է «բար»).:

`wget {{[-O|--output-document]}} {{bar}} {{https://example.com/foo}}`

- Ներբեռնեք մեկ վեբ էջ և դրա բոլոր ռեսուրսները հարցումների միջև 3 վայրկյան ընդմիջումներով (սկրիպտներ, ոճաթերթեր, պատկերներ և այլն):

`wget {{[-pkw|--page-requisites --convert-links --wait]}} 3 {{https://example.com/some_page.html}}`

- Ներբեռնեք բոլոր թվարկված ֆայլերը գրացուցակի և դրա ենթագրքերում (չի ներբեռնում ներկառուցված էջի տարրերը).:

`wget {{[-mnp|--mirror --no-parent]}} {{https://example.com/some_path/}}`

- Սահմանափակեք ներբեռնման արագությունը և միացման կրկնությունների քանակը.:

`wget --limit-rate {{300k}} {{[-t|--tries]}} {{100}} {{https://example.com/some_path/}}`

- Ներբեռնեք ֆայլ HTTP սերվերից՝ օգտագործելով Basic Auth-ը (գործում է նաև FTP-ի համար).:

`wget --user {{username}} --password {{password}} {{https://example.com}}`

- Շարունակեք թերի ներբեռնումը.:

`wget {{[-c|--continue]}} {{https://example.com}}`

- Ներբեռնեք տեքստային ֆայլում պահված բոլոր URL-ները որոշակի գրացուցակում.:

`wget {{[-P|--directory-prefix]}} {{path/to/directory}} {{[-i|--input-file]}} {{path/to/URLs.txt}}`
