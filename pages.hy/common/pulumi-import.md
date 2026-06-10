# pulumi ներմուծում

> Ներմուծեք ռեսուրսներ գոյություն ունեցող կույտում:.
> Կարդացեք շարահյուսությունը ձեր ամպային մատակարարի համար՝ <https://www.pulumi.com/registry/>:.
> Լրացուցիչ տեղեկություններ. <https://www.pulumi.com/docs/iac/cli/commands/pulumi_import/>:.

- Ստեղծեք ռեսուրսի սահմանումը գոյություն ունեցող մատակարարի ռեսուրսի համար տրված անունով.:

`pulumi import {{type_token}} {{name}} {{id}}`

- Ներմուծեք գոյություն ունեցող AWS օգտվողին որպես `pulumi` ռեսուրս.:

`pulumi import aws:iam/user:User {{my_user_resource}} {{id}}`

- Ներմուծեք գոյություն ունեցող Cloudflare աշխատող.:

`pulumi import cloudflare:index/workersScript:WorkersScript {{my_worker_script}} {{account_id/script_name}}`

- Ներմուծեք JSON ֆայլից զանգվածային ներմուծման գործառնությունների համար և դուրս բերեք ֆայլ՝ `stdout`-ի փոխարեն:

`pulumi import --file {{path/to/file.json}} --out {{path/to/file}}`
