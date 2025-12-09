# wodim

> Command (aliased as `cdrecord` on some systems) for recording data to CDs or DVDs.
> Some invocations of wodim can cause destructive actions, such as erasing all the data on a disc.
> More information: <https://manned.org/wodim>.

- Display optical drives available to `wodim`:

`wodim --devices`

- Record ("burn") an audio-only disc:

`wodim dev={{/dev/optical_drive}} -audio {{track*.cdaudio}}`

- Burn a file to a disc, ejecting the disc once done (some recorders require this):

`wodim -eject dev={{/dev/optical_drive}} -data {{file.iso}}`

- Burn a file to the disc in an optical drive, potentially writing to multiple discs in succession:

`wodim -tao dev={{/dev/optical_drive}} -data {{file.iso}}`
