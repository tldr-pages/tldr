# eval

> Execute arguments as a single command in the current shell and return its result.
> More information: <https://www.gnu.org/software/bash/manual/bash.html#index-eval>.

- Call `echo` with the "foo" argument:

`eval "{{echo foo}}"`

- Set a variable in the current shell:

`eval "{{foo=bar}}"`
