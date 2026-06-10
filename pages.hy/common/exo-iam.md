# exo iam

> Կառավարեք Exoscale IAM ծառայությունը:.
> Լրացուցիչ տեղեկություններ. <https://community.exoscale.com/product/iam/>:.

- Թվարկեք IAM-ի բոլոր դերերը.:

`exo iam role list`

- Ստեղծեք նոր API բանալի.:

`exo iam api-key create {{api_key_name}} {{iam_role_name}}`

- Ստեղծեք նոր IAM դեր.:

`cat {{path/to/policy.json}} | exo iam role create {{iam_role_name}} --editable --policy -`

- Ցույց տալ գոյություն ունեցող IAM դերի քաղաքականությունը.:

`exo iam role show {{iam_role_name}} --policy {{[-O|--output-format]}} {{json}} | jq .`

- Թարմացրեք կանխադրված Կազմակերպության քաղաքականությունը (Կազմակերպության կանխադրված քաղաքականությունը կկիրառվի Կազմակերպության բոլոր API ստեղների վրա).:

`cat {{path/to/policy.json}} | exo iam org-policy update -`
