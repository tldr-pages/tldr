# amass

> Map attack surfaces and discover assets.
> Some subcommands such as `enum` and `intel` have their own usage documentation.
> More information: <https://github.com/owasp-amass/amass>.

- Discover subdomains for a domain:

`amass enum -d {{domain_name}}`

- Perform passive-only enumeration (no direct contact with the target):

`amass enum -passive -d {{domain_name}}`

- Enumerate subdomains using a config file:

`amass enum -config {{path/to/config.ini}} -d {{domain_name}}`

- Gather intelligence about an organization:

`amass intel -org "{{organization_name}}"`

- Display the database of previously enumerated results:

`amass db -show`

- Display help for a subcommand:

`amass {{enum|intel|db|viz}} -help`
