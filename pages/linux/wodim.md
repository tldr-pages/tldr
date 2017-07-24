# wodim

> Command for record/burning data using a optical drive to CD or DVD.
> Some usage of wodim can cause destructive actions, such as erasing all the data on a disc.

- Display optical drives avaliable to wodim:

`wodim --devices`

- Display help switches for use with wodim:

`cdrecord`

- Record a pure CD-DA audio:

`wodim dev=/dev/{{optical_drive}} -audio {{track*.cdaudio}}`

- Burn a file to disc in optical drive where the disc will be ejected after recording (this is needed for some devices):

`wodim -eject dev=/dev/{{optical_drive}} -data {{file.iso}}`

- Burn a file to disc in optical drive, with the option to record to the same disc over multiple sessions:

`wodim -tao dev=/dev/{{optical_drive}} -data {{file.iso}}`
