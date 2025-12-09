# trust

> Operate on the trust policy store.
> More information: <https://manned.org/trust>.

- List trust policy store items:

`trust list`

- List information about specific items in the trust policy store:

`trust list --filter={{blocklist|ca-anchors|certificates|trust-policy}}`

- Store a specific trust anchor in the trust policy store:

`trust anchor {{path/to/certificate.crt}}`

- Remove a specific anchor from the trust policy store:

`trust anchor --remove {{path/to/certificate.crt}}`

- Extract trust policy from the shared trust policy store:

`trust extract --format=x509-directory --filter=ca-anchors {{path/to/directory}}`

- Display help for a subcommand:

`trust {{subcommand}} --help`
