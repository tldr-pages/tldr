# scdoc

> Generate `man` manual pages.
> More information: <https://github.com/ddevault/scdoc>.

- Generate man pages from a scdoc (.sdc) file:

`scdoc < file.scd > file.1`

- Generate man pages from a scdoc file and pipe to a pager:

`scdoc < file.scd | {{less}}`
