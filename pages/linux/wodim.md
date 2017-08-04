# wodim

> Command for record/burning data using a optical drive to CD or DVD.
> This command is also called cdrecord on some systems, but it is wodim underneath.
> Some usage of wodim can cause destructive actions, such as erasing all the data on a disc.

- Display optical drives available to wodim:

`wodim --devices`

- Record pure CD-DA audio to a disc:

`wodim dev=/dev/{{optical_drive}} -audio {{track*.cdaudio}}`

- Burn a file to a disc, ejecting the disc once done (some recorders require this):

`wodim -eject dev=/dev/{{optical_drive}} -data {{file.iso}}`

- Burn a file to the disc in an optical drive, potentially writing to multiple discs in succession:

`wodim -tao dev=/dev/{{optical_drive}} -data {{file.iso}}`
