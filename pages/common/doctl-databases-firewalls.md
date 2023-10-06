# doctl databases firewalls

> Manage specific databases that are served by a database cluster.
> More information: <https://docs.digitalocean.com/reference/doctl/reference/databases/firewalls/>.

- Run a doctl databases firewalls command with an access token:

`doctl databases firewalls [command] --access-token {{ access_token }}`

- Retrieve a list of firewall rules for a given database:

`doctl databases firewalls list`

- Add a database firewall rule to a given database:

`doctl databases firewalls append {{ database id }} --rule {{ type (droplet, k8s, ip_addr, tag, or app) }}:{{ value }}`

- Remove a firewall rule for a given database:

`doctl databases firewalls remove {{ database id }} {{ rule uuid }}`