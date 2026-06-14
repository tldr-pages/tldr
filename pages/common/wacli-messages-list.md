# wacli messages list

> List messages from a WhatsApp chat.
> See also: `wacli messages search`, `wacli messages show`, `wacli messages context`.

- List messages from a specific chat in JSON format:

`wacli messages list --chat {{phone_number}}@s.whatsapp.net --json`

- List messages received after a specific date:

`wacli messages list --chat {{phone_number}}@s.whatsapp.net --after {{2026-01-28}} --json`

- List messages received before a specific date:

`wacli messages list --chat {{phone_number}}@s.whatsapp.net --before {{2026-01-28}} --json`

- List messages within a date range:

`wacli messages list --chat {{phone_number}}@s.whatsapp.net --after {{2026-01-01}} --before {{2026-01-31}} --json`

- Limit the number of results:

`wacli messages list --chat {{phone_number}}@s.whatsapp.net --limit {{10}} --json`
