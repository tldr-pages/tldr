# fprintd-verify

> Verify fingerprints against the database.
> More information: <https://manned.org/fprintd-verify>.

- Verify all stored fingerprints for the current user:

`fprintd-verify`

- Verify a specific fingerprint for the current user:

`fprintd-verify --finger {{left-thumb|left-index-finger|left-middle-finger|left-ring-finger|left-little-finger|right-thumb|right-index-finger|right-middle-finger|right-ring-finger|right-little-finger}}`

- Verify fingerprints for a specific user:

`fprint-verify {{username}}`

- Verify a specific fingerprint for a specific user:

`fprintd-verify --finger {{finger_name}} {{username}}`

- Fail the process if a fingerprint doesn't match with ones stored in the database for the current user:

`fprint-verify --g-fatal-warnings`

- Display help:

`fprintd-verify --help`
