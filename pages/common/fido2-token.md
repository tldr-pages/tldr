# fido2-token

> Find and manage a FIDO2 authenticator.
> More information: <https://developers.yubico.com/libfido2/Manuals/fido2-token.html>.

- List all FIDO2 authenticators:

`fido2-token -L`

- Display information about a specific authenticator:

`fido2-token -I {{device}}`

- List relying parties with discoverable credentials stored on an authenticator:

`fido2-token -L -r {{device}}`

- List discoverable credentials for a specific relying party (usually a domain name):

`fido2-token -L -k {{relying_party_id}} {{device}}`

- Delete a discoverable credential by its base64-encoded ID:

`fido2-token -D -i {{credential_id}} {{device}}`

- Set or change the authenticator's PIN:

`fido2-token {{-S|-C}} {{device}}`

- Reset an authenticator to default factory settings:

`fido2-token -R {{device}}`
