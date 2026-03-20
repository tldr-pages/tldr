# cdrecord

> Record data to CDs or DVDs.
> Some invocations of cdrecord can cause destructive actions, such as erasing all the data on a disc.
> More information: <https://manpages.debian.org/bookworm/wodim/cdrecord.1.en.html>.

- List available optical recorders:

`cdrecord --devices`

- Burn an ISO image to a disc and eject it when done:

`cdrecord -eject dev={{/dev/optical_drive}} -data {{path/to/file.iso}}`

- Burn audio tracks to a disc:

`cdrecord dev={{/dev/optical_drive}} -audio {{path/to/track1.wav}} {{path/to/track2.wav}}`

- Test a burn without writing to the disc:

`cdrecord -dummy dev={{/dev/optical_drive}} -data {{path/to/file.iso}}`

- Quickly blank a rewritable disc:

`cdrecord dev={{/dev/optical_drive}} blank=fast`
