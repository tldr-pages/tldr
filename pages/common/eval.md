# eval

> Execute arguments as a single command in the current shell and return its result.
> More information: <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#eval>.

- Call `echo` with the "foo" argument:

`eval "{{echo foo}}"`

- Set a variable in the current shell:

`eval "{{foo=bar}}"`
