# run-mailcap

> Execute programs via entries in the mailcap file.
> More information: <https://manned.org/run-mailcap>.

- Compose any existing file or new on default mailcap edit tool:

`run-mailcap --action=compose {{filename}}`

- View any file on default mailcap explorer:

`run-mailcap --action=edit {{filename}}`

- Print any file on default run-mailcap tool:

`run-mailcap --action=print {{filename}}`

- View any file (usually image) on default mailcap explorer:

`run-mailcap --action=view {{filename}}`

- Invoke individual actions/programs on run-mailcap:

`run-mailcap --action={{view|cat|compose|composetyped|edit|print}} {{path/to/file}}`

- Turn on extra information:

`run-mailcap --action={{action}} --debug {{path/to/file}}`

- Ignore any "copiousoutput" directive and forward output to `stdout`:

`run-mailcap --action={{action}} --nopager {{path/to/file}}`

- Display the found command without actually executing it:

`run-mailcap --action={{action}} --norun {{path/to/file}}`
