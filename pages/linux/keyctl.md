# keyctl

> Manipulate the Linux kernel keyring.
> More information: <https://manned.org/keyctl>.

- List keys in a specific keyring:

`keyctl list {{target_keyring}}`

- List current keys in the user default session:

`keyctl list @us`

- Store a key in a specific keyring:

`keyctl add {{type_keyring}} {{key_name}} {{key_value}} {{target_keyring}}`

- Store a key with its value on the standard input:

`echo -n {{key_value}} | keyctl padd {{type_keyring}} {{key_name}} {{target_keyring}}`

- Put a timeout on a key:

`keyctl timeout {{key_name}} {{timeout_in_seconds}}`

- Read a key and formats it as a hex-dump if not printable:

`keyctl read {{key_name}}`

- Read a key and formats as-is:

`keyctl pipe {{key_name}}`

- Revoke a key and prevents any further action on it:

`keyctl revoke {{key_name}}`
