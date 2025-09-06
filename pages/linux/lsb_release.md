# lsb_release

> Get LSB (Linux Standard Base) and distribution-specific information.
> More information: <https://manned.org/lsb_release>.

- Print all available information:

`lsb_release {{[-a|--all]}}`

- Print a description (usually the full name) of the operating system:

`lsb_release {{[-d|--description]}}`

- Print only the operating system name (ID), suppressing the field name:

`lsb_release {{[-is|--id --short]}}`

- Print the release number and codename of the distribution, suppressing the field names:

`lsb_release {{[-rcs|--release --codename --short]}}`
