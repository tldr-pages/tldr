# wacli contacts search

> Search WhatsApp contacts by name.
> See also: `wacli contacts show`, `wacli contacts refresh`.
> More information: <https://wacli.sh/contacts.html>.

- Search for contacts by name in JSON format:

`wacli contacts search "{{name}}" --json`

- Search for contacts using a custom store:

`wacli contacts search "{{name}}" --json --store {{path/to/store}}`
