# cli4

> Python command-line interface for Cloudflare API.
> More information: <https://github.com/cloudflare/python-cloudflare>.

- Display account information:

`cli4 {{/user}}`

- List all zones:

`cli4 {{/zones}}`

- List DNS records for a specific zone:

`cli4 {{/zones/:example.com/dns_records}}`

- Create a new DNS record:

`cli4 --post {{name=example.com}} {{type=A}} {{content=192.0.2.1}} {{/zones/:example.com/dns_records}}`

- Update an existing DNS record:

`cli4 --put {{name=sub.example.com}} {{type=A}} {{content=192.0.2.2}} {{/zones/:example.com/dns_records/:record_id}}`

- Delete a DNS record:

`cli4 --delete {{/zones/:example.com/dns_records/:record_id}}`

- Purge all cache for a zone:

`cli4 --post {{purge_everything=true}} {{/zones/:example.com/purge_cache}}`
