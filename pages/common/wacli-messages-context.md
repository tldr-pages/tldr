# wacli messages context

> Display messages surrounding a specific WhatsApp message.
> See also: `wacli messages show`, `wacli messages list`.

- Show context around a specific message in JSON format:

`wacli messages context {{message_id}} --json`

- Show context around a message using a custom store:

`wacli messages context {{message_id}} --json --store {{path/to/store}}`
