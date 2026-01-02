# hwinfo

> Probe for the hardware present in the system.
> See also: `inxi`, `lshw`.
> More information: <https://manpages.opensuse.org/hwinfo/hwinfo.8.en.html>.

- Display all available hardware information:

`hwinfo`

- Display information about a specific hardware component:

`hwinfo --{{cpu|memory|disk|gfxcard|network|usb|pci|keyboard|mouse|monitor|sound|fingerprint|...}}`

- Display information about a specific hardware component succinctly:

`hwinfo {{--component}} --short`

- Write all hardware information to a file:

`hwinfo --all --log {{path/to/file}}`

- Display help:

`hwinfo --help`
