# run-mailcap

> Run MailCap Programs.
> Run mailcap view, see, edit, compose, print - execute programs via entries in the mailcap file (or any of its aliases) will use the given action to process each mime-type/file.
> More information: <https://manned.org/run-mailcap>.

- Individual actions/programs on run-mailcap can be invoked with action flag:

`run-mailcap --action=ACTION [--option[=value]]`

- In simple language:

`run-mailcap --action=ACTION {{path/to/file}}`

- Turn on extra information:

`run-mailcap --action=ACTION --debug {{path/to/file}}`

- Ignore any "copiousoutput" directive and forward output to standard output:

`run-mailcap --action=ACTION --nopager {{path/to/file}}`

- Display the found command without actually executing it:

`run-mailcap --action=ACTION --norun {{path/to/file}}`
