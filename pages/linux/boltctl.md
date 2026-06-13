# boltctl

> Control thunderbolt devices.
> More information: <https://manned.org/boltctl>.

- List connected (and authorized) devices:

`boltctl`

- List connected devices, including unauthorized ones:

`boltctl list`

- Authorize a device temporarily:

`boltctl authorize {{device_uuid}}`

- Authorize and remember a device:

`boltctl enroll {{device_uuid}}`

- Revoke a previously authorized device:

`boltctl forget {{device_uuid}}`

- Show more information about a device:

`boltctl info {{device_uuid}}`
