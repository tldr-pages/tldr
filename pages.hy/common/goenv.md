# goenv

> Տեղադրեք, տեղահանեք կամ անցեք Golang տարբերակների միջև:.
> Աջակցում է տարբերակների համարներին, ինչպիսիք են «1.16.15» կամ «1.22.8» և այլն:.
> Լրացուցիչ տեղեկություններ. <https://github.com/go-nv/goenv>:.

- Թվարկեք բոլոր հասանելի goenv հրամանները.:

`goenv commands`

- Տեղադրեք Golang-ի կոնկրետ տարբերակը.:

`goenv install {{go_version}}`

- Օգտագործեք Golang-ի կոնկրետ տարբերակը ընթացիկ նախագծում.:

`goenv local {{go_version}}`

- Սահմանեք Golang-ի լռելյայն տարբերակը.:

`goenv global {{go_version}}`

- Թվարկեք Golang-ի բոլոր հասանելի տարբերակները և ընդգծեք կանխադրվածը.:

`goenv versions`

- Տեղահանեք Go-ի տրված տարբերակը.:

`goenv uninstall {{go_version}}`

- Գործարկեք գործարկվող տարբերակը ընտրված Go տարբերակով.:

`goenv exec go run {{go_version}}`
