#մուլվադ

> CLI հաճախորդ Mullvad VPN-ի համար:.
> Տես նաև՝ `fastd`, `ivpn`, `mozillavpn`, `warp-cli`:.
> Լրացուցիչ տեղեկություններ. <https://mulllvad.net/en/help/how-use-mulllvad-cli>:.

- Կապեք ձեր Mullvad հաշիվը նշված հաշվի համարով.:

`mullvad account set {{account_number}}`

- Միացնել LAN մուտքը, քանի դեռ VPN-ը միացված է.:

`mullvad lan set allow`

- Ընտրեք սերվեր կոնկրետ քաղաքում.:

`mullvad relay set location {{se}} {{mma}}`

- Ընտրեք հատուկ սերվեր.:

`mullvad relay set location {{se-mma-wg-001}}`

- Ստեղծեք VPN թունելը.:

`mullvad connect`

- Ստուգեք VPN թունելի կարգավիճակը.:

`mullvad status`

- Ստուգեք հաշվի գործողության ժամկետը և ստացեք սարքի անունը.:

`mullvad account get`
