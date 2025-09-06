# whereis

> Locate the binary, source, and manual page files for a command.
> More information: <https://manned.org/whereis>.

- Locate binary, source and man pages for SSH:

`whereis {{ssh}}`

- Locate [b]inary and [m]an pages for ls:

`whereis -bm {{ls}}`

- Locate [s]ource of gcc and [m]an pages for Git:

`whereis -s {{gcc}} -m {{git}}`

- Locate [b]inaries for gcc in `/usr/bin/` only:

`whereis -b -B {{/usr/bin/}} -f {{gcc}}`

- Locate [u]nusual binaries (those that have more or less than one binary on the system):

`whereis -u *`

- Locate binaries that have [u]nusual [m]anual entries (binaries that have more or less than one manual installed):

`whereis -u -m *`
