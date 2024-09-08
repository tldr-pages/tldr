# pamsplit

> Split a multi-image Netpbm file into multiple single-image Netpbm files.
> See also: `pamfile`, `pampick`, `pamexec`.
> More information: <https://netpbm.sourceforge.net/doc/pamsplit.html>.

- Split a multi-image Netpbm file into multiple single-image Netpbm files:

`pamsplit {{path/to/image.pam}}`

- Specify a pattern for naming output files:

`pamsplit {{path/to/image.pam}} {{file_%d.pam}}`
