# չեկով

> Ստատիկ կոդի վերլուծության գործիք Ենթակառուցվածքի համար որպես կոդ (IaC):.
> Սա նաև ծրագրային կազմի վերլուծության (SCA) գործիք է պատկերների և բաց կոդով փաթեթների համար:.
> Լրացուցիչ տեղեկություններ. <https://www.checkov.io/1.Welcome/Quick%20Start.html>:.

- Սկանավորեք IaC պարունակող գրացուցակը (Terraform, Cloudformation, ARM, Ansible, Bicep, Dockerfile և այլն):

`checkov --directory {{path/to/directory}}`

- Սկանավորեք IaC ֆայլը՝ բաց թողնելով կոդի բլոկները ելքի մեջ.:

`checkov --compact --file {{path/to/file}}`

- Նշեք բոլոր ստուգումները IaC-ի բոլոր տեսակների համար.:

`checkov --list`
