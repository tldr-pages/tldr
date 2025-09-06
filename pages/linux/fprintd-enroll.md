# fprintd-enroll

> Enroll fingerprints into the database.
> More information: <https://manned.org/fprintd-enroll>.

- Enroll the right index finger for the current user:

`fprintd-enroll`

- Enroll a specific finger for the current user:

`fprintd-enroll {{[-f|--finger]}} {{left-thumb|left-index-finger|left-middle-finger|left-ring-finger|left-little-finger|right-thumb|...}}`

- Enroll the right index finger for a specific user:

`fprintd-enroll {{username}}`

- Enroll a specific finger for a specific user:

`fprintd-enroll {{[-f|--finger]}} {{finger_name}} {{username}}`

- Display help:

`fprintd-enroll --help`
