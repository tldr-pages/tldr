# vhs

> CLI home video recorder to generate terminal gifs from code.
> More information: <https://github.com/charmbracelet/vhs>.

- Create a tape file (Add commands to the tap file using your editor):

`vhs new {{path/to/file.tape}}`

- Record inputs to a tape file (Once done, exit the shell to create the tape):

`vhs record > {{path/to/file.tape}}`

- Record inputs to a tape file using a specific shell:

`vhs record --shell {{shell}} > {{path/to/file.tape}}`

- Validate a type file's syntax:

`vhs validate {{path/to/file.tape}}`

- Create a gif from a tape file:

`vhs < {{path/to/file.tape}}`

- Publish a gif to https://vhs.charm.sh and get a shareable URL:

`vhs publish {{path/to/file.gif}}`
