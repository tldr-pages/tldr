# boltctl

> Dispozitive de control fulger.
> Mai multe informaţii: <https://manned.org/boltctl>

- Lista dispozitivelor conectate (și autorizate):

`boltctl`

- Lista dispozitivelor conectate, inclusiv cele neautorizate:

`boltctl list`

- Autorizarea temporară a unui dispozitiv:

`boltctl authorize {{device_uuid}}`

- Autorizează și reține un dispozitiv:

`boltctl enroll {{device_uuid}}`

- Revocarea unui dispozitiv autorizat anterior:

`boltctl forget {{device_uuid}}`

- Afișați mai multe informații despre un dispozitiv:

`boltctl info {{device_uuid}}`
