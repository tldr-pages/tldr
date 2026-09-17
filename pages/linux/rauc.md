# rauc

> Lightweight update client for Embedded Linux devices to create, inspect and install update bundles.
> More information: <https://manned.org/rauc>.

- Display the current system status and slot overview:

`rauc status`

- Install an update bundle:

`rauc install {{path/to/bundle.raucb|https://example.com/bundle.raucb}}`

- Show information about a specific update bundle:

`rauc info {{path/to/bundle.raucb}}`

- Create a signed update bundle from a directory:

`rauc bundle --cert {{path/to/cert.pem}} --key {{path/to/key.pem}} {{path/to/input_dir}} {{path/to/output.raucb}}`

- Extract the contents of an update bundle:

`rauc extract {{path/to/bundle.raucb}} {{path/to/output_directory}}`

- Mark the currently booted slot as good to confirm successful update:

`rauc status mark-good`

- Mark a specific slot as bad to prevent it from booting:

`rauc status mark-bad {{slot_name}}`

- Switch the active boot slot to the other available slot:

`rauc status mark-active other`
