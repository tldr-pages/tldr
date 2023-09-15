# linode-cli domains

> Manage Linode Domains and DNS configuration.
> See also: `linode-cli`.
> More information: <https://www.linode.com/docs/products/tools/cli/guides/domains/>.

- List all managed domains:

`linode-cli domains list`

- Create a new managed domain:

`linode-cli domains create --domain {{domain_name}} --type {{master|slave}} --soa-email {{email}}`

- View details of a specific domain:

`linode-cli domains view {{domain_id}}`

- Delete a managed domain:

`linode-cli domains delete {{domain_id}}`

- List records for a specific domain:

`linode-cli domains records-list {{domain_id}}`

- Add a DNS record to a domain:

`linode-cli domains records-create {{domain_id}} --type {{A|AAAA|CNAME|MX|...}} --name {{subdomain}} --target {{target_value}}`

- Update a DNS record for a domain:

`linode-cli domains records-update {{domain_id}} {{record_id}} --target {{new_target_value}}`

- Delete a DNS record from a domain:

`linode-cli domains records-delete {{domain_id}} {{record_id}}`
