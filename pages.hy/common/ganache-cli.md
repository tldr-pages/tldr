# ganache-cli

> Ganache-ի հրամանի տող տարբերակը՝ ձեր անձնական բլոկչեյնը Ethereum-ի զարգացման համար:.
> Լրացուցիչ տեղեկություններ. <https://archive.trufflesuite.com/ganache/>:.

- Գործարկել Ganache:

`ganache-cli`

- Գործարկեք Ganache-ը որոշակի թվով հաշիվներով.:

`ganache-cli --accounts={{number_of_accounts}}`

- Գործարկեք Ganache-ը և կողպեք հասանելի հաշիվները լռելյայն.:

`ganache-cli --secure`

- Գործարկեք Ganache սերվերը և բացեք հատուկ հաշիվներ.:

`ganache-cli --secure --unlock "{{account_private_key1}}" --unlock "{{account_private_key2}}"`

- Գործարկեք Ganache-ը հատուկ հաշվի և մնացորդի հետ.:

`ganache-cli --account="{{account_private_key}},{{account_balance}}"`

- Գործարկեք Ganache-ը լռելյայն մնացորդով հաշիվներով.:

`ganache-cli --defaultBalanceEther={{default_balance}}`

- Գործարկեք Ganache-ը և գրանցեք բոլոր հարցումները `stdout`:

`ganache-cli --verbose`
