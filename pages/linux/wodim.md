# wodim

> Command for record/burning data using a optical drive to CD or DVD.
> Caution when using this command.
> There are many ways this command can be destructive, the following below is meant as a reminder of wodims syntax and not as the only source of documentation.

- Display optical drives avaliable to wodim:

`wodim --devices`

- Burn file to disc in optical drive:

`wodim -eject -tao speed=0 dev=/dev/{{optical_drive}} -v -data /{{file.iso}}`

- Record a pure CD-DA audio:

`wodim -v speed=1 dev=/dev/{{optical_drive}} -audio {{track*.cdaudio}}`
