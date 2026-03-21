# wacli messages search

> Search WhatsApp messages using full-text search.
> See also: `wacli messages list`, `wacli messages show`.

- Search messages in a specific chat:

`wacli messages search "{{query}}" --chat {{phone_number}}@s.whatsapp.net --json`

- Search messages from a specific sender:

`wacli messages search "{{query}}" --from {{phone_number}}@s.whatsapp.net --json`

- Search messages after a specific date:

`wacli messages search "{{query}}" --chat {{phone_number}}@s.whatsapp.net --after {{2026-01-28}} --json`

- Search messages of a specific type:

`wacli messages search "{{query}}" --type {{image|video|audio|document}} --json`

- Search messages with a result limit:

`wacli messages search "{{query}}" --chat {{phone_number}}@s.whatsapp.net --limit {{10}} --json`
