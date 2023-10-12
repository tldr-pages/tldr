# doctl databases firewalls

> Manage firewalls for database clusters.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/firewalls>.

- Run a `doctl databases firewalls` command with an access token:

`doctl databases firewalls {{command}} --access-token {{access_token}}`

- Retrieve a list of firewall rules for a given database:

`doctl databases firewalls list`

- Add a database firewall rule to a given database:

`doctl databases firewalls append {{database_id}} --rule {{droplet|k8s|ip_addr|tag|app}}:{{value}}`

- Remove a firewall rule for a given database:

`doctl databases firewalls remove {{database_id}} {{rule_uuid}}`
