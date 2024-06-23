# whereis

> Locate the binary, source, and manual page files for a command.
> More information: <https://manned.org/whereis>.

- Locate binary, source and man pages for SSH:

`whereis {{ssh}}`

- Locate binary and man pages for ls:

`whereis -bm {{ls}}`

- Locate source of gcc and man pages for Git:

`whereis -s {{gcc}} -m {{git}}`

- Locate binaries for gcc in `/usr/bin/` only:

`whereis -b -B {{/usr/bin/}} -f {{gcc}}`

- Locate unusual binaries (those that have more or less than one binary on the system):

`whereis -u *`

- Locate binaries that have unusual manual entries (binaries that have more or less than one manual installed):

`whereis -u -m *`
