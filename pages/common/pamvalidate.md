# pamvalidate

> Validate PAM, PGM, PBM and PPM files.
> See also: `pamfile`, `pamfix`.
> More information: <https://netpbm.sourceforge.net/doc/pamvalidate.html>.

- Copy a Netpbm file from `stdin` to `stdout` if and only if it valid; fail otherwise:

`{{command}} | pamvalidate > {{path/to/output.ext}}`
