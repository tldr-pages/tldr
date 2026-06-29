# nak

> The Nostr army knife: generate keys, build and sign events, and query relays from the command line.
> More information: <https://github.com/fiatjaf/nak>.

- Generate a new secret key:

`nak key generate`

- Compute the public key from a secret key:

`nak key public {{secret_key}}`

- Decode a NIP-19 entity (npub, note, nevent) to hex/JSON:

`nak decode {{nostr_entity}}`

- Fetch the latest events of a given kind from a relay:

`nak req --kind {{1}} --limit {{10}} {{wss://relay_url}}`

- Fetch all events from a specific author:

`nak req --author {{hex_pubkey}} {{wss://relay_url}}`

- Sign and publish a text note to one or more relays:

`nak event --kind {{1}} --content "{{message}}" --sec {{secret_key}} {{wss://relay_url}}`

- Verify an event's signature and hash:

`nak verify '{{event_json}}'`
