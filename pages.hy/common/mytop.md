# mytop

> Ցուցադրել MySQL սերվերի աշխատանքի մասին տեղեկությունները, ինչպիսիք են `top`:.
> Լրացուցիչ տեղեկություններ. <https://jeremy.zawodny.com/mysql/mytop/mytop.html>:.

- Սկսել `mytop`:

`mytop`

- Միացեք նշված օգտվողի անունով և գաղտնաբառով.:

`mytop {{[-u|-user]}} {{user}} {{[-p|-password]}} {{password}}`

- Միացեք նշված օգտվողի անունով (օգտատիրոջը կառաջարկվի գաղտնաբառ).:

`mytop {{[-u|-user]}} {{user}} -prompt`

- Մի ցուցադրեք պարապ (քնած) թելեր.:

`mytop {{[-u|-user]}} {{user}} {{[-p|-password]}} {{password}} --noidle`
