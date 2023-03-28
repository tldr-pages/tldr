# vhs

> Generate Terminal Gifs from Code.
> More information: <https://github.com/charmbracelet/vhs>.

- Record inputs to a tape file (Once done, exit the shell to create the tape):

`vhs record > {{tape_name}}`

- Record inputs to a tape file using a specific shell:

`vhs record --shell {{shell}} > cassette.tape`

- Validate a type file's syntax:

`vhs validate {{tape_name_or_path}}`

- Create gif from tape File:

`vhs < {{tape_name_or_path}}.tape`

- Publish a gif to vhs.charm.sh and get a shareable url:

`vhs publish {{path/to/gif}}`
