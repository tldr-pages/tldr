# in-toto-sign

> Մուտք գործեք հղում կամ դասավորեք մետատվյալները կամ ստուգեք դրանց ստորագրությունները:.
> Լրացուցիչ տեղեկություններ. <https://in-toto.readthedocs.io/en/latest/command-line-tools/in-toto-sign.html>:.

- Երկու ստեղներով ստորագրեք «unsigned.layout» և գրեք «root.layout»՝:

`in-toto-sign {{[-f|--file]}} {{unsigned.layout}} {{[-k|--keep]}} {{priv_key1}} {{priv_key2}} {{[-o|--output]}} {{root.layout}}`

- Փոխարինեք ստորագրությունը հղման ֆայլում և գրեք լռելյայն ֆայլի անվանմանը.:

`in-toto-sign {{[-f|--file]}} {{package.2f89b927.link}} {{[-k|--keep]}} {{priv_key}}`

- Ստուգեք 3 ստեղներով ստորագրված դասավորությունը.:

`in-toto-sign {{[-f|--file]}} {{root.layout}} {{[-k|--keep]}} {{pub_key0}} {{pub_key1}} {{pub_key2}} --verify`

- Ստորագրեք դասավորությունը լռելյայն GPG ստեղնով լռելյայն GPG ստեղնաշարի մեջ.:

`in-toto-sign {{[-f|--file]}} {{root.layout}} {{[-g|--gpg]}}`

- Ստուգեք դասավորությունը GPG ստեղնով, որը նույնականացված է «...439F3C2» ստեղնաշարով:

`in-toto-sign {{[-f|--file]}} {{root.layout}} --verify {{[-g|--gpg]}} {{...439F3C2}}`
