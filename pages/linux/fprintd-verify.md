# fprintd-verify

> Verify fingerprints against the database.
> More information: <https://manned.org/fprintd-verify>.

- Verify all stored fingerprints for the current user:

`fprintd-verify`

- Verify a specific fingerprint for the current user:

`fprintd-verify  {{[-f|--finger]}} {{left|right}}-{{thumb|index-finger|middle-finger|ring-finger|little-finger}}`

- Verify fingerprints for a specific user:

`fprint-verify {{username}}`

- Verify a specific fingerprint for a specific user:

`fprintd-verify {{[-f|--finger]}} {{finger_name}} {{username}}`

- Fail the process if a fingerprint doesn't match with ones stored in the database for the current user:

`fprint-verify --g-fatal-warnings`

- Display help:

`fprintd-verify --help`
