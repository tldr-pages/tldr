# linode-cli հանգույցների հավասարակշռիչներ

> Կառավարեք Linode NodeBalancers-ը:.
> Տես նաև՝ `linode-cli`:.
> Լրացուցիչ տեղեկություններ. <https://techdocs.akamai.com/cloud-computing/docs/cli-commands-for-nodebalancers>:.

- Թվարկեք բոլոր NodeBalancer-ները.:

`linode-cli nodebalancers list`

- Ստեղծեք նոր NodeBalancer.:

`linode-cli nodebalancers create --region {{region}}`

- Դիտեք կոնկրետ NodeBalancer-ի մանրամասները.:

`linode-cli nodebalancers view {{nodebalancer_id}}`

- Թարմացրեք գոյություն ունեցող NodeBalancer-ը.:

`linode-cli nodebalancers update {{nodebalancer_id}} --label {{new_label}}`

- Ջնջել NodeBalancer-ը.:

`linode-cli nodebalancers delete {{nodebalancer_id}}`

- Նշեք NodeBalancer-ի կոնֆիգուրացիաները.:

`linode-cli nodebalancers configs list {{nodebalancer_id}}`

- Ավելացնել նոր կոնֆիգուրացիա NodeBalancer-ում.:

`linode-cli nodebalancers configs create {{nodebalancer_id}} --port {{port}} --protocol {{protocol}}`
