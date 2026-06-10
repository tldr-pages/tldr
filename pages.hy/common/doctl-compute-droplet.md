# doctl հաշվարկային կաթիլ

> Ցուցակել, ստեղծել և ջնջել վիրտուալ մեքենաները, որոնք կոչվում են կաթիլներ:.
> Լրացուցիչ տեղեկություններ. <https://docs.digitalocean.com/reference/doctl/reference/compute/droplet/>:.

- Ստեղծեք կաթիլ.:

`doctl compute {{[d|droplet]}} {{[c|create]}} --region {{region}} --image {{os_image}} --size {{vps_type}} {{droplet_name}}`

- Ջնջել մի կաթիլ.:

`doctl compute {{[d|droplet]}} {{[d|delete]}} {{droplet_id|droplet_name}}`

- Ցուցակ կաթիլներ.:

`doctl compute {{[d|droplet]}} {{[ls|list]}}`
