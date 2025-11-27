# scdoc

> Generate `man` manual pages.
> More information: <https://git.sr.ht/~sircmpwn/scdoc/tree/master/item/scdoc.1.scd>.

- Generate man pages from a scdoc (`.scd`) file:

`scdoc < {{path/to/file.scd}} > {{path/to/file.1}}`

- Generate man pages from a scdoc file and display the generated troff (man) source:

`scdoc < {{path/to/file.scd}} | {{less}}`
