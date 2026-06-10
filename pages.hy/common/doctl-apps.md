# doctl հավելված

> Կառավարեք DigitalOcean հավելվածները:.
> Լրացուցիչ տեղեկություններ. <https://docs.digitalocean.com/reference/doctl/reference/apps/>:.

- Ստեղծեք հավելված.:

`doctl {{[a|apps]}} {{[c|create]}}`

- Ստեղծեք տեղակայում կոնկրետ հավելվածի համար.:

`doctl {{[a|apps]}} {{[cd|create-deployment]}} {{app_id}}`

- Ջնջել հավելվածը ինտերակտիվ կերպով.:

`doctl {{[a|apps]}} {{[d|delete]}} {{app_id}}`

- Ստացեք հավելված.:

`doctl {{[a|apps]}} {{[g|get]}}`

- Թվարկեք բոլոր հավելվածները.:

`doctl {{[a|apps]}} {{[ls|list]}}`

- Թվարկեք բոլոր տեղակայումները հատուկ հավելվածից.:

`doctl {{[a|apps]}} {{[lsd|list-deployments]}} {{app_id}}`

- Ստացեք տեղեկամատյաններ հատուկ հավելվածից.:

`doctl {{[a|apps]}} {{[l|logs]}} {{app_id}}`

- Թարմացրեք որոշակի հավելված տվյալ հավելվածի սպեկտրով.:

`doctl {{[a|apps]}} {{[u|update]}} {{app_id}} --spec {{path/to/spec.yml}}`
