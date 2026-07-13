# wacli messages show

> Display a specific WhatsApp message by its ID.
> See also: `wacli messages list`, `wacli messages context`.
> More information: <https://wacli.sh/messages.html>.

- Show a specific message in JSON format:

`wacli messages show {{message_id}} --json`

- Show a specific message using a custom store:

`wacli messages show {{message_id}} --json --store {{path/to/store}}`
