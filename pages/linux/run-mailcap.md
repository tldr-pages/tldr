# run-mailcap

> Run MailCap Programs.
> Run mailcap view,  see,  edit,  compose, print - execute programs via entries in the mailcap file (or any of its  aliases)  will  use  the  given  action  to process  each  mime-type/file.

- Individual actions/programs on run-mailcap can be invoked with action flag:

`run-mailcap --action=ACTION [--option[=value]]`

- In simple language:

`run-mailcap --action=ACTION {{filename}}`

- Turn on extra information:

`run-mailcap --debug --action=ACTION {{options}}`

- Ignore any "copiousoutput" directive and forward output to STD‐OUT:

`--nopager`

- Display the found command without actually executing it:

`--norun`
