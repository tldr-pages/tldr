# doctl տվյալների բազաների firewalls

> Կառավարեք firewalls տվյալների բազայի կլաստերների համար:.
> Լրացուցիչ տեղեկություններ. <https://docs.digitalocean.com/reference/doctl/reference/databases/firewalls/>:.

- Գործարկեք `doctl databases firewalls` հրամանը մուտքի նշանով.:

`doctl {{[d|databases]}} {{[fw|firewalls]}} {{command}} {{[-t|--access-token]}} {{access_token}}`

- Առբերեք firewall-ի կանոնների ցանկը տվյալ տվյալների բազայի համար.:

`doctl {{[d|databases]}} {{[fw|firewalls]}} {{[ls|list]}}`

- Տվյալ տվյալների բազայի վրա ավելացնել տվյալների բազայի firewall կանոն.:

`doctl {{[d|databases]}} {{[fw|firewalls]}} {{[a|append]}} {{database_id}} --rule {{droplet|k8s|ip_addr|tag|app}}:{{value}}`

- Հեռացրեք firewall կանոնը տվյալ տվյալների բազայի համար.:

`doctl {{[d|databases]}} {{[fw|firewalls]}} {{[rm|remove]}} {{database_id}} {{rule_uuid}}`
