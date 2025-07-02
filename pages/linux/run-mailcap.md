# run-mailcap

> Run MailCap Programs.
> Run mailcap view, see, edit, compose, print - execute programs via entries in the mailcap file (or any of its aliases) will use the given action to process each mime-type/file.
> More information: <https://manned.org/run-mailcap>.

- Individual actions/programs on run-mailcap can be invoked with action flag:

`run-mailcap --action={{view|cat|compose|composetyped|edit|print}}`

- In simple language:

`run-mailcap --action={{action}} {{filename}}`

- Turn on extra information:

`run-mailcap --action={{action}} --debug {{filename}}`

- Ignore any "copiousoutput" directive and forward output to `stdout`:

`run-mailcap --action={{action}} --nopager {{filename}}`

- Display the found command without actually executing it:

`run-mailcap --action={{action}} --norun {{filename}}`
