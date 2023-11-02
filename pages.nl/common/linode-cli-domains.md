# linode-cli domains

> Beheer Linode Domains en DNS configuratie.
> Bekijk ook: `linode-cli`.
> Meer informatie: <https://www.linode.com/docs/products/tools/cli/guides/domains/>.

- Toon alle beheerde domeinen:

`linode-cli domains list`

- Maak een nieuw beheerd domein:

`linode-cli domains create --domain {{domein_naam}} --type {{master|slave}} --soa-email {{email}}`

- Bekijk details van een specifiek domein:

`linode-cli domains view {{domein_id}}`

- Verwijder een beheerd domein:

`linode-cli domains delete {{domein_id}}`

- Toon records voor een specifiek domein:

`linode-cli domains records-list {{domein_id}}`

- Voeg een DNS record toe aan een domein:

`linode-cli domains records-create {{domein_id}} --type {{A|AAAA|CNAME|MX|...}} --name {{subdomein}} --target {{target_value}}`

- Update een DNS record voor een domein:

`linode-cli domains records-update {{domein_id}} {{record_id}} --target {{new_target_value}}`

- Verwijder een DNS record van een domein:

`linode-cli domains records-delete {{domein_id}} {{record_id}}`
