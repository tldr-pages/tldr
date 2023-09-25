# hwinfo

> hwinfo is used to probe for the hardware present in the system. It can be used
> to generate a system overview log which can be later used for support.
> More information: <https://github.com/openSUSE/hwinfo>.

- Get graphics card information:

`hwinfo --gfxcard`

- Get network information:

`hwinfo --network`

- See other type of hardware items:

`hwinfo --help`

- Abbreviate the output:

`hwinfo --short --disk --cdrom`

- Write all hardward info to file:

`hwinfo --all --log={{path/to/file}}`
