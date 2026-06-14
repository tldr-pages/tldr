# az մուտք

> Մուտք գործեք Azure:.
> `azure-cli`-ի մի մասը (հայտնի է նաև որպես `az`):.
> Լրացուցիչ տեղեկություններ. <https://learn.microsoft.com/cli/azure/reference-index#az-login>:.

- Մուտք գործեք ինտերակտիվ կերպով.:

`az login`

- Մուտք գործեք ծառայության տնօրենի հետ՝ օգտագործելով հաճախորդի գաղտնիքը.:

`az login --service-principal {{[-u|--username]}} {{http://azure-cli-service-principal}} {{[-p|--password]}} {{secret}} {{[-t|--tenant]}} {{someone.onmicrosoft.com}}`

- Մուտք գործեք ծառայության տնօրենի հետ՝ օգտագործելով հաճախորդի վկայականը.:

`az login --service-principal {{[-u|--username]}} {{http://azure-cli-service-principal}} {{[-p|--password]}} {{path/to/cert.pem}} {{[-t|--tenant]}} {{someone.onmicrosoft.com}}`

- Մուտք գործեք՝ օգտագործելով VM համակարգի հատկացված ինքնությունը.:

`az login {{[-i|--identity]}}`

- Մուտք գործեք՝ օգտագործելով VM-ի օգտատիրոջ ինքնությունը՝:

`az login {{[-i|--identity]}} {{[-u|--username]}} /subscriptions/{{subscription_id}}/resourcegroups/{{my_rg}}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{{my_id}}`
