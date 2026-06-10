# pip ինդեքս

> Ստուգեք փաթեթի ինդեքսներից հասանելի տեղեկատվությունը:.
> Լրացուցիչ տեղեկություններ. <https://pip.pypa.io/en/stable/cli/pip_index/>:.

- Թվարկեք փաթեթի բոլոր հասանելի տարբերակները.:

`pip index versions {{package}}`

- Թվարկեք տարբերակները որոշակի ինդեքսից.:

`pip index versions {{package}} --index-url {{https://test.pypi.org/simple/}}`

- Ներառեք նախնական թողարկման տարբերակները.:

`pip index versions {{package}} --pre`

- Ներառեք լրացուցիչ ցուցանիշ.:

`pip index versions {{package}} --extra-index-url {{https://example.com/simple/}}`

- Թվարկեք տարբերակները որոշակի հարթակի համար.:

`pip index versions {{package}} --platform {{linux_x86_64}}`
