# linode-cli domains

> Command-line interface to manage Linode Domains and DNS via `linode-cli`.

- List all managed domains:

`linode-cli domains list`

- Create a new managed domain:

`linode-cli domains create --domain [domain-name] --type [master/slave] --soa-email [email]`

- View details of a specific domain:

`linode-cli domains view [domain-id]`

- Delete a managed domain:

`linode-cli domains delete [domain-id]`

- List records for a specific domain:

`linode-cli domains records-list [domain-id]`

- Add a DNS record to a domain:

`linode-cli domains records-create [domain-id] --type [A/AAAA/CNAME/MX/etc.] --name [subdomain] --target [target-value]`

- Update a DNS record for a domain:

`linode-cli domains records-update [domain-id] [record-id] --target [new-target-value]`

- Delete a DNS record from a domain:

`linode-cli domains records-delete [domain-id] [record-id]`
