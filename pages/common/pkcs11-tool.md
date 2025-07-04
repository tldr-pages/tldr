# pkcs11-tool

> Utility for managing and using PKCS #11 security tokens.
> More information: <https://github.com/OpenSC/OpenSC/wiki/Using-pkcs11-tool-and-OpenSSL>.

- List slots and their potential token, using a specific module (e.g. `/usr/lib/softhsm/libsofthsm2.so`):

`pkcs11-tool --module {{path/to/module.so}} {{[-L|--list-slots]}} {{[-T|--list-token-slots]}}`

- List objects in a specific slot. (Note: `slot_id` is not the slot index shown as "Slot X"):

`pkcs11-tool {{[-O|--list-objects]}} {{[-p|--pin]}} {{auth_pin}} --slot {{slot_id}}`

- Create a new object with a specific label and type:

`pkcs11-tool --slot {{slot_id}} {{[-p|--pin]}} {{auth_pin}} {{[-y|--type]}} {{cert|privkey|pubkey|secrkey|data|...}} {{[-a|--label]}} "{{label}}" {{[-d|--id]}} {{01}} {{[-w|--write-object]}} {{path/to/cert.crt}}`

- Delete an object by its label and type:

`pkcs11-tool --slot {{slot_id}} {{[-p|--pin]}} {{auth_pin}} {{[-y|--type]}} {{cert|privkey|pubkey|secrkey|data|...}} {{[-a|--label]}} "{{label}}" {{[-b|--delete-object]}}`
