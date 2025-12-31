# lsb_release

> Get LSB (Linux Standard Base) and distribution-specific information.
> More information: <https://manned.org/lsb_release>.

- Print all available information:

`lsb_release {{[-a|--all]}}`

- Print a description (usually the full name) of the operating system:

`lsb_release {{[-d|--description]}}`

- Print only the operating system name (ID), in short format (omitting the field name):

`lsb_release {{[-is|--id --short]}}`

- Print the release number and codename of the distribution, in short format:

`lsb_release {{[-rcs|--release --codename --short]}}`
