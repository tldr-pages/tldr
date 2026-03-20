# cdrecord

> Record data to CDs or DVDs.
> Some invocations of cdrecord can cause destructive actions, such as erasing all the data on a disc.
> More information: <https://manned.org/cdrecord>.

- Display optical drives available to `cdrecord`:

`cdrecord --devices`

- Record ("burn") an audio-only disc:

`cdrecord dev={{/dev/optical_drive}} -audio {{track*.cdaudio}}`

- Burn a file to a disc, ejecting the disc once done (some recorders require this):

`cdrecord -eject dev={{/dev/optical_drive}} -data {{file.iso}}`

- Burn a file to the disc in an optical drive, potentially writing to multiple discs in succession:

`cdrecord -tao dev={{/dev/optical_drive}} -data {{file.iso}}`
