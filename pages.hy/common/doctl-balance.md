# doctl հաշվեկշիռ

> Ցույց տալ Digital Ocean հաշվի մնացորդը:.
> Լրացուցիչ տեղեկություններ. <https://docs.digitalocean.com/reference/doctl/reference/balance/>:.

- Ստացեք ընթացիկ համատեքստի հետ կապված հաշվի մնացորդը.:

`doctl balance {{[g|get]}}`

- Ստացեք մուտքի նշանի հետ կապված հաշվի մնացորդը.:

`doctl balance {{[g|get]}} {{[-t|--access-token]}} {{access_token}}`

- Ստացեք հաշվի մնացորդը, որը կապված է որոշակի համատեքստի հետ.:

`doctl balance {{[g|get]}} --context`
