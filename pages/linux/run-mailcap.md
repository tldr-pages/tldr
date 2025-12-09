# run-mailcap

> Run MailCap Programs.
> Run mailcap view, see, edit, compose, print - execute programs via entries in the mailcap file (or any of its aliases) will use the given action to process each mime-type/file.
> More information: <https://manned.org/run-mailcap>.

- Invoke individual actions/programs on run-mailcap:

`run-mailcap --action={{view|cat|compose|composetyped|edit|print}} {{path/to/file}}`

- Turn on extra information:

`run-mailcap --action={{action}} --debug {{path/to/file}}`

- Ignore any "copiousoutput" directive and forward output to `stdout`:

`run-mailcap --action={{action}} --nopager {{path/to/file}}`

- Display the found command without actually executing it:

`run-mailcap --action={{action}} --norun {{path/to/file}}`
